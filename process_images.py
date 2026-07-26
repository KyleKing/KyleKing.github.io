"""Strip metadata from the source photographs and build the derivatives the page serves.

Run after any change to the photographs, by hand or through the pre-commit hook.

Originals are rewritten in place because they are published to a public site, so
any GPS coordinates or camera identifiers in them would be public too. Stripping
metadata also discards the orientation tag, so that rotation is baked into the
pixels first. Derivatives are rebuilt only when missing or older than their source.
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


def _derive(source: Path, dest: Path, max_edge: int, quality: int) -> bool:
    if dest.is_file() and dest.stat().st_mtime >= source.stat().st_mtime:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as img:
        img.thumbnail((max_edge, max_edge), Image.LANCZOS)
        img.convert('RGB').save(
            dest, 'JPEG', quality=quality, optimize=True, progressive=True
        )
    return True


def main() -> None:
    root = Path(__file__).parent
    sources = sorted((root / SOURCE_DIR).glob('*.jpeg'))
    portrait = root / PORTRAIT

    stripped = sum(_strip_metadata(path) for path in [*sources, portrait])
    written = sum(
        _derive(source, root / directory / source.name, edge, quality)
        for source in sources
        for directory, edge, quality in (
            (THUMB_DIR, THUMB_EDGE, THUMB_QUALITY),
            (DISPLAY_DIR, DISPLAY_EDGE, DISPLAY_QUALITY),
        )
    )
    print(f'{len(sources)} photos: stripped {stripped}, wrote {written} derivatives')


if __name__ == '__main__':
    main()
