# /// script
# requires-python = ">=3.12"
# dependencies = ["pillow"]
# ///
"""Compress the photographs the items page serves and discard the originals.

Run with `uv run process_images.py`, or let the pre-commit hook run it on any
change to the photographs.

Drop full-size photographs into SOURCE_DIR. Each one is resized into a THUMB_DIR
and a DISPLAY_DIR copy carrying no metadata, and the original is then deleted, so
a photograph taken at home never reaches a public site with its GPS coordinates
attached. Deleting also keeps originals out of git history from here on, though
anything already committed stays in history and is recoverable from there.

Metadata includes the orientation tag, so rotation is baked into the pixels
first. DISPLAY_EDGE is the highest resolution that survives.

The portrait on the personal site is served directly and so is stripped in place
rather than resized.
"""

from pathlib import Path

from PIL import Image, ImageOps
from PIL.JpegImagePlugin import get_sampling

from generate_whatsapp import DISPLAY_DIR, DISPLAY_EDGE, SOURCE_DIR, THUMB_DIR, THUMB_EDGE

ORIENTATION_TAG = 274
PORTRAIT = Path('IMG_0428.jpeg')
THUMB_QUALITY = 78
DISPLAY_QUALITY = 82


def _strip_metadata(path: Path) -> bool:
    """Rewrite the photograph without metadata. Returns whether it had any."""
    with Image.open(path) as img:
        if not img.getexif():
            return False
        if img.getexif().get(ORIENTATION_TAG, 1) == 1:
            img.load()
            cleaned, params = img, {'quality': 'keep'}
        else:
            # Rotating forces a re-encode, so carry the source's own tables
            # across rather than letting a fixed quality inflate the file.
            cleaned = ImageOps.exif_transpose(img)
            params = {'qtables': img.quantization, 'subsampling': get_sampling(img)}
        staged = path.with_name(path.name + '.tmp')
        cleaned.save(staged, 'JPEG', optimize=True, **params)
    staged.replace(path)
    return True


def _derive(source: Path, dest: Path, max_edge: int, quality: int) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as img:
        oriented = ImageOps.exif_transpose(img)
        oriented.thumbnail((max_edge, max_edge), Image.LANCZOS)
        oriented.convert('RGB').save(
            dest, 'JPEG', quality=quality, optimize=True, progressive=True
        )


def _compress(source: Path, root: Path) -> None:
    """Write both sizes, then delete the original once they are on disk."""
    sizes = (
        (root / THUMB_DIR / source.name, THUMB_EDGE, THUMB_QUALITY),
        (root / DISPLAY_DIR / source.name, DISPLAY_EDGE, DISPLAY_QUALITY),
    )
    for dest, max_edge, quality in sizes:
        _derive(source, dest, max_edge, quality)
    if all(dest.is_file() for dest, _, _ in sizes):
        source.unlink()


def main() -> None:
    root = Path(__file__).parent
    sources = sorted((root / SOURCE_DIR).glob('*.jpeg'))
    for source in sources:
        _compress(source, root)
    stripped = _strip_metadata(root / PORTRAIT)
    print(f'compressed and removed {len(sources)} originals, stripped {int(stripped)} portrait')


if __name__ == '__main__':
    main()
