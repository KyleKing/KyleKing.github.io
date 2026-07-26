"""Generate the static items page from the hardcoded ITEMS list.

The page owns its own visual world and does not inherit from DESIGN.md, which
governs index.html only. See .impeccable/surfaces/ for the surface brief.

Items titled 'TBD' are placeholders and are never emitted. Every image path a
non-placeholder item references must exist, or generation fails.

TODO: Serve thumbnails from build-time derivatives. The photo directory is
~60 MB and every thumbnail currently loads a full-resolution original, so a
72px square costs several megabytes on a phone. Resizing here would need
Pillow, which the pre-commit hook's interpreter is not guaranteed to have.
"""

import re
from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from textwrap import dedent
from urllib.parse import urlparse

PLACEHOLDER_TITLE = 'TBD'


class ItemStatus(StrEnum):
    FREE = 'free'
    PAID = 'paid'
    PENDING = 'pending'


@dataclass(frozen=True)
class Item:
    title: str
    image_paths: list[Path]
    status: ItemStatus
    link: str
    description: str
    price: str


ITEMS: list[Item] = [
    Item(
        title=title,
        image_paths=[Path('whatsapp-items') / img for img in image_names],
        status=ItemStatus(status),
        link=link,
        description=description,
        price=price,
    )
    for title, image_names, status, link, description, price in [
        (
            'UPPAbaby Vista Bassinet (Bassinet only) + Bug and Rain Covers',
            ('Baby-Bassinet-Open.jpeg', 'Baby-Bassinet-Closed.jpeg', 'Baby-Bassinet-Packed.jpeg',),
            ItemStatus.PAID,
            'https://babytochild.com/uppababy-bassinet-review-safe-overnight-sleep-or-just-smart-stroller-add-on',
            dedent("""\
            This is the v2 Bassinet, but it works with either v2 or v3 stroller (Vista, Cruz, and Ridge). Our UPPAbaby
            Vista stroller isn't for sale right now so this listing is only for the bassinet"""),
            '$75 or MX$1500',
        ),
        (
            'Ingenuity Soothe \'n Delight Foldable Baby Swing and 6-Speeds (0-9 Months, 6-20 lbs)',
            ('Baby-Swing-1.jpeg','Baby-Swing-2.jpeg','Baby-Swing-3.jpeg'),
            ItemStatus.PAID,
            'https://www.amazon.com/Ingenuity-Comfort-Go-Portable-Swing/dp/B00E3RKC36?th=1',
            dedent("""\
            Includes batteries and only lightly used. Sold new for $70"""),
            '$40 or MX$750',
        ),
        (
            'Ergobaby Embrace Newborn Baby Carrier (0-12 Months, 7-25 lbs)',
            ('Baby-Carrier.jpeg',),
            ItemStatus.PAID,
            'https://ergobaby.com/en-us/products/embrace-newborn-carrier',
            dedent("""\
            Soft olive color and like new. Recommended by the WireCutter"""),
            '$75 or MX$1500',
        ),
        (
            'Bobbie Organic Infant Formula (Gentle)',
            ('Baby-Bobbie-Formula-Gentle.jpeg',),
            ItemStatus.PAID,
            'https://www.hibobbie.com/products/bobbie-organic-gentle-infant-formula?variant=40549922046037',
            dedent("""\
            All unopened and good until August 2027"""),
            '$25/each or $150 for all seven',
        ),
        (
            'Bobbie Organic Infant Formula',
            ('Baby-Bobbie-Formula-Organic.jpeg',),
            ItemStatus.PAID,
            'https://www.hibobbie.com/products/bobbie-organic-infant-formula?variant=32828253667413',
            dedent("""\
            All unopened and good until August 2027"""),
            '$20/each or $140 for all eight',
        ),
        (
            'Decrypto (Limited 5th Edition Box)',
            ('Games-Decrypto-1.jpeg', 'Games-Decrypto-4.jpeg', 'Games-Decrypto-5.jpeg'),
            ItemStatus.PAID,
            'https://boardgamegeek.com/boardgame/225694/decrypto',
            dedent("""\
            New in shrink wrap because I accidentally ordered two"""),
            '$25 or MX$500',
        ),
        (
            'Geared (Kickstarter Edition)',
            ('Games-Geared-Open.jpeg', 'Games-Geared-Box.jpeg'),
            ItemStatus.PAID,
            'https://www.kickstarter.com/projects/815894852/geared-build-your-bike',
            dedent("""\
            Played five or so timtes and in very good condition!"""),
            '$5 or MX$100',
        ),
        (
            'Love Letter',
            ('Games-LoveLetter-Open.jpeg', 'Games-LoveLetter-Box.jpeg'),
            ItemStatus.PAID,
            'https://boardgamegeek.com/boardgame/129622/love-letter',
            dedent("""\
            Played a dozen times and in very good condition!"""),
            '$7 or MX$150',
        ),
        (
            'Sushi Go',
            ('Games-SushiGo-Open.jpeg', 'Games-SushiGo-Box.jpeg'),
            ItemStatus.PAID,
            'https://boardgamegeek.com/boardgame/133473/sushi-go',
            dedent("""\
            Played around ten times and in very good condition!"""),
            '$5 or MX$100',
        ),
        (
            'Ticket to Ride Europe + 1912 Expansion',
            ( 'Games-TTR-Open.jpeg', 'Games-TTR-Box.jpeg',),
            ItemStatus.PAID,
            'https://boardgamegeek.com/boardgameexpansion/53383/ticket-to-ride-europa-1912',
            dedent("""\
            Such a great game, but I now have too many games. I would be willing to sell the Europa expansion
            separately (~$12), but I no longer have the box for it"""),
            '$35 or MX$700',
        ),
        (
            'Whirling Witchraft',
            ( 'Games-WW-Open.jpeg', 'Games-WW-Box.jpeg',),
            ItemStatus.PAID,
            'https://boardgamegeek.com/boardgame/335275/whirling-witchcraft',
            dedent("""\
            Played once and in very good condition"""),
            '$20 or MX$400',
        ),
        (
            'Tsuro',
            (
                'Games-Tsuro-Open-2.jpeg',
                'Games-Tsuro-Open-1.jpeg',
                'Games-Tsuro-Box.jpeg',
            ),
            ItemStatus.PAID,
            'https://www.amazon.com/dp/B002SQBB3O?tag=itemtext-boardgamegeek-20&linkCode=ogi&th=1&psc=1',
            dedent("""\
            Played around ten times and in very good condition!"""),
            '$20 or MX$400',
        ),
        (
            'Toniebox (Broken! For parts)',
            ('Home-BrokenTony-2.jpeg', 'Home-BrokenTony-3.jpeg'),
            ItemStatus.FREE,
            '',
            dedent("""\
            We have already received a replacement, because the first one would suddenly stop playing and shutdown. They
            never clarified what was wrong, but the speakers, battery, and other parts might be of interest? You might
            be able to drop in a Raspberry Pi Zero in place of the motherboard if adventurous. It doesn't look like you
            can buy replacement boards and replacing the transistor or other shorted components is involved to salvage
            it fully"""),
            '',
        ),
        (
            'Assorted Velcro Sanding Discs with Drill Attachment Pad',
            ('Home-Sanding.jpeg',),
            ItemStatus.FREE,
            'https://www.amazon.com/dp/B088CXY3X5?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1&th=1',
            dedent("""\
            These work ok, but I needed to resurface a wooden bowl, which required buying a stronger orbital sander"""),
            '',
        ),
        (
            'Kate Spade Macaron Mug',
            ('Home-KS-Mug-Up.jpeg', 'Home-KS-Mug-Down.jpeg',),
            ItemStatus.FREE,
            '',
            '',
            '',
        ),
        (
            'Away Orange Drawstring Kids Bag',
            ('Home-Away-Bag.jpeg',),
            ItemStatus.FREE,
            '',
            'This came with an Away suitcase and sized smaller than most drawstring bags, but we don\'t have a use for it',
            '',
        ),
        (
            'VIGRUE 175PCS Assorted Concrete Screws Kit',
            ('Home-Nails.jpeg',),
            ItemStatus.PAID,
            'https://www.amazon.com/dp/B0CJT845WJ?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1&th=1',
            dedent("""\
            We bought this last year, but ended up not needing it"""),
            '$10 or MX$200',
        ),
        (
            'Scalpers Brown Leather Wallet',
            ('Wallet-01-Flat.jpeg', 'Wallet-04-Back.jpeg'),
            ItemStatus.PAID,
            'https://en.ww.scalperscompany.com/products/61778-scmondit-free-wallet-aw2526-brown',
            dedent("""\
            I received this as a gift, but I had already gotten a new wallet. Made from 100% Cow Leather.
            The wallet has the original tags, if you would like to give it as a gift"""),
            '$20 or MX$400',
        ),
        (
            'ARRIS SurfBoard SB6141 Modem',
            ('Home-Modem.jpeg',),
            ItemStatus.FREE,
            'https://www.amazon.com/ARRIS-SURFboard-SB6141-DOCSIS-Cable/dp/B00AJHDZSI',
            dedent("""\
            We can't use this modem with Telmex because it requires a regular Ethernet hookup, but it may work with other providers here or be useful for parts"""),
            '',
        ),
        (
            'IKEA Hugad Curtain Rod (Rod only)',
            ('Home-Rod-2.jpeg','Home-Rod-0.jpeg'),
            ItemStatus.FREE,
            'https://www.ikea.com/us/en/p/hugad-curtain-rod-white-10217141/#content',
            dedent("""\
            We gave away the blackout curtains that we used with this rod, but I didn't find it until doing
            a deep clean this week. Free to anyone who could use it!"""),
            '',
        ),
    ]
]

DIRECTION_CONTRACT = """<!--
THESIS: A neighbourhood offer list reads as the manifest it already is,
numbered lines on a form, and refuses the e-commerce grid of equal cards.
OWN-WORLD: Neutral form stock, one black ink, and a dispatch-orange marking ink
spent only on what is free. Archivo at normal proportions: caps for the heading,
tracked caps for field labels, tabular figures down the price column. Rules
carry every division. No shadows, no rounded cards, no color fields.
STORY: A neighbour sees what is on offer, judges condition from the
photographs, reads an honest price, and messages in the building chat.
FIRST VIEWPORT: A compact form header (title, standfirst, then six fields:
pickup, lines, split, terms, to claim, updated) closed by a heavy rule, with
the first five numbered lines already on screen beneath it.
FORM: Packing manifest, candidate 4 of the grounded list, no staging (physics
drop-assembly rejected: needs an engine this dependency-free page cannot carry,
and it fights the phone-scan job). Seed bed3738d.
-->"""

HEAD_HTML = """
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="Board games, baby gear, and household items, free or for sale in East Polanco, Mexico City" />
<meta name="theme-color" content="#f2f2f0" media="(prefers-color-scheme: light)" />
<meta name="theme-color" content="#131312" media="(prefers-color-scheme: dark)" />
<meta name="robots" content="noindex" />
<title>Free &amp; For Sale &middot; Polanco</title>

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Archivo:wght@400..900&display=swap"
  rel="stylesheet"
/>

<style>
  :root {
    --ground: #f2f2f0;
    --surface: #ffffff;
    --ink: #131311;
    --ink-soft: #54544f;
    --rule: #cfcfc9;
    --mark: #c33505;
    --photo: #e6e6e2;
    --ease: cubic-bezier(0.16, 1, 0.3, 1);
    interpolate-size: allow-keywords;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --ground: #131312;
      --surface: #1c1c1a;
      --ink: #e6e5e0;
      --ink-soft: #9b9b93;
      --rule: #333330;
      --mark: #ff713f;
      --photo: #232320;
    }
  }

  *,
  *::before,
  *::after {
    box-sizing: border-box;
  }

  body {
    background: var(--ground);
    color: var(--ink);
    font-family: "Archivo", "Helvetica Neue", Arial, sans-serif;
    font-size: 1rem;
    margin: 0;
  }

  .label {
    color: var(--ink-soft);
    font-size: 0.6875rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    line-height: 1.2;
    text-transform: uppercase;
  }

  .wrap {
    margin: 0 auto;
    max-width: 74rem;
    padding: 0 1.25rem;
  }

  /* Masthead: the form header of the manifest */
  .masthead {
    border-bottom: 2px solid var(--ink);
  }
  .masthead .wrap {
    padding-bottom: 1.25rem;
    padding-top: 1.75rem;
  }
  .masthead h1 {
    font-size: clamp(1.75rem, 5.5vw, 2.5rem);
    font-weight: 700;
    letter-spacing: 0.005em;
    line-height: 1.05;
    margin: 0 0 0.4rem 0;
    text-transform: uppercase;
    text-wrap: balance;
  }
  .masthead .standfirst {
    color: var(--ink-soft);
    font-size: 1rem;
    margin: 0 0 1.25rem 0;
    max-width: 58ch;
  }

  .fields {
    border-top: 1px solid var(--rule);
    display: grid;
    gap: 1.125rem 1.5rem;
    grid-template-columns: repeat(auto-fit, minmax(7.5rem, 1fr));
    margin: 0;
    padding-top: 1.125rem;
  }
  .fields div {
    min-width: 0;
  }
  .fields dt {
    margin-bottom: 0.3rem;
  }
  .fields dd {
    font-size: 0.9375rem;
    font-weight: 500;
    line-height: 1.35;
    margin: 0;
  }
  main {
    padding-bottom: 5rem;
  }

  .section-head {
    align-items: baseline;
    display: flex;
    flex-wrap: wrap;
    font-size: 1.125rem;
    font-weight: 700;
    gap: 0.65rem;
    letter-spacing: 0.08em;
    margin: 2.75rem 0 0.85rem 0;
    text-transform: uppercase;
  }
  .section-count {
    margin-left: auto;
  }
  .section-anchor {
    color: var(--ink-soft);
    font-size: 1rem;
    font-weight: 500;
    text-decoration: none;
  }
  .section-anchor:hover,
  .section-anchor:focus-visible {
    color: var(--mark);
  }

  .manifest {
    border-top: 2px solid var(--ink);
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .line {
    border-bottom: 1px solid var(--rule);
  }
  .line > summary {
    align-items: center;
    cursor: pointer;
    display: grid;
    gap: 1rem;
    grid-template-columns: 2rem 4.5rem minmax(0, 1fr) auto;
    list-style: none;
    padding: 1.05rem 0.25rem;
  }
  .line > summary::-webkit-details-marker {
    display: none;
  }
  .line:hover:not([open]) {
    background: var(--surface);
  }
  .line > summary:focus-visible {
    outline: 2px solid var(--mark);
    outline-offset: -2px;
  }

  .line-no {
    color: var(--ink-soft);
    font-size: 0.75rem;
    font-variant-numeric: tabular-nums;
    font-weight: 700;
    letter-spacing: 0.06em;
    padding: 0.15rem 0;
    text-align: center;
    transition: background 200ms var(--ease), color 200ms var(--ease);
  }
  .line[open] .line-no {
    background: var(--ink);
    color: var(--ground);
  }

  .thumb {
    aspect-ratio: 1;
    background: var(--photo);
    overflow: hidden;
    position: relative;
  }
  .thumb img {
    display: block;
    height: 100%;
    object-fit: cover;
    width: 100%;
  }
  .shots {
    background: var(--ink);
    bottom: 0;
    color: var(--ground);
    font-size: 0.625rem;
    font-variant-numeric: tabular-nums;
    font-weight: 700;
    padding: 0.1rem 0.32rem;
    position: absolute;
    right: 0;
  }

  .line-title {
    font-size: 1.0625rem;
    overflow-wrap: break-word;
    font-weight: 600;
    line-height: 1.25;
    text-wrap: pretty;
  }

  .price {
    font-variant-numeric: tabular-nums;
    font-weight: 700;
    text-align: right;
    white-space: nowrap;
  }
  .price .mx {
    color: var(--ink-soft);
    display: block;
    font-size: 0.8125rem;
    font-weight: 500;
  }
  .price.is-free {
    color: var(--mark);
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }
  .price.is-pending {
    color: var(--ink-soft);
    font-size: 0.875rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  /* The authored moment: an opened line feeds out like a printout */
  .line::details-content {
    block-size: 0;
    overflow: hidden;
    transition: block-size 420ms var(--ease),
      content-visibility 420ms var(--ease) allow-discrete;
  }
  .line[open]::details-content {
    block-size: auto;
  }

  .detail {
    display: grid;
    gap: 1.25rem;
    padding: 0.5rem 0.25rem 2rem 0.25rem;
  }
  @media (min-width: 62rem) {
    .detail {
      padding-left: 8.75rem;
    }
  }

  .gallery {
    display: grid;
    gap: 0.5rem;
    grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
    margin: 0;
  }
  /* Portrait-leaning frame: these are phone photographs, and contain never
     crops away the wear a buyer is trying to see. */
  .gallery img {
    animation: feed 520ms var(--ease) both;
    animation-delay: calc(var(--i) * 70ms);
    aspect-ratio: 3 / 4;
    background: var(--photo);
    display: block;
    object-fit: contain;
    width: 100%;
  }
  @keyframes feed {
    from {
      clip-path: inset(0 0 100% 0);
    }
    to {
      clip-path: inset(0 0 0 0);
    }
  }

  .desc {
    line-height: 1.65;
    margin: 0;
    max-width: 68ch;
    text-wrap: pretty;
  }

  .detail-foot {
    align-items: baseline;
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem 1.5rem;
  }
  .ref,
  .permalink {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-decoration-thickness: 1px;
    text-transform: uppercase;
    text-underline-offset: 0.28em;
  }
  .ref {
    color: var(--mark);
  }
  .permalink {
    color: var(--ink-soft);
  }
  .ref:focus-visible,
  .permalink:focus-visible {
    outline: 2px solid var(--mark);
    outline-offset: 3px;
  }


  .sr-only {
    border-width: 0;
    clip: rect(0, 0, 0, 0);
    height: 1px;
    margin: -1px;
    overflow: hidden;
    padding: 0;
    position: absolute;
    white-space: nowrap;
    width: 1px;
  }

  @media (max-width: 30rem) {
    .masthead .wrap {
      padding-top: 1.75rem;
    }
    .masthead .standfirst {
      margin-bottom: 1.25rem;
    }
    /* Ruled form rows, so the header does not eat the whole phone screen */
    .fields {
      gap: 0.6rem;
      grid-template-columns: 1fr;
    }
    .fields div {
      align-items: baseline;
      display: flex;
      gap: 0.75rem;
    }
    .fields dt {
      flex: 0 0 4.75rem;
      margin-bottom: 0;
    }
    /* The title needs the full column width, so the price drops beneath it */
    .line > summary {
      gap: 0.4rem 0.85rem;
      grid-template-columns: 1.75rem 5.5rem minmax(0, 1fr);
    }
    .gallery {
      gap: 0.35rem;
    }
    .detail {
      padding-left: 0;
      padding-right: 0;
    }
    .line-no,
    .thumb {
      grid-row: 1 / 3;
    }
    .price {
      grid-column: 3;
      text-align: left;
      white-space: normal;
    }
    .price .mx {
      display: inline;
      margin-left: 0.4rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .line::details-content,
    .line-no {
      transition: none;
    }
    .gallery img {
      animation: none;
    }
  }
</style>
</head>
"""

# A deep link should open the line it names; the accordion itself is native.
SCRIPT_HTML = """<script>
const openTarget = () => {
  const line = document.querySelector(location.hash ? `details${location.hash}` : null);
  if (line) {
    line.open = true;
    line.scrollIntoView({block: 'start'});
  }
};
window.addEventListener('hashchange', openTarget);
if (location.hash) openTarget();
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const openCard = document.querySelector('details[open]');
    if (openCard) {
      openCard.open = false;
    }
  }
});
</script>"""


def _slug(title: str) -> str:
    return 'item-' + re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', title.lower())).strip('-')


def _price_html(item: Item) -> str:
    if item.status is ItemStatus.PENDING:
        return '<span class="price is-pending">Pending</span>'
    if not item.price:
        return '<span class="price is-free">Free<span class="sr-only">, no charge</span></span>'
    usd, _, mxn = item.price.partition(' or ')
    mxn_html = f'<span class="mx">{mxn}</span>' if mxn else ''
    return f'<span class="price">{usd}{mxn_html}</span>'


def _gallery_html(item: Item) -> str:
    images = [
        f'<img src="{path.as_posix()}" alt="{item.title}, photo {n} of {len(item.image_paths)}" '
        f'style="--i:{n - 1}" loading="lazy" decoding="async" />'
        for n, path in enumerate(item.image_paths, start=1)
    ]
    return f'<div class="gallery">{"".join(images)}</div>'


def _line_html(item: Item, line_no: int, eager: bool) -> str:
    slug = _slug(item.title)
    shots = (
        f'<span class="shots">{len(item.image_paths)}<span class="sr-only"> photos</span></span>'
        if len(item.image_paths) > 1
        else ''
    )
    loading = 'eager' if eager else 'lazy'
    desc = f'<p class="desc">{item.description}</p>' if item.description else ''
    host = urlparse(item.link).netloc.removeprefix('www.')
    ref = (
        f'<a class="ref" href="{item.link}" target="_blank" rel="noopener noreferrer">'
        f'View on {host}<span class="sr-only">, opens in a new tab</span></a>'
        if item.link
        else ''
    )
    return f"""
        <li>
          <details class="line" id="{slug}" name="manifest">
            <summary>
              <span class="line-no">{line_no:02d}</span>
              <span class="thumb">
                <img src="{item.image_paths[0].as_posix()}" alt="" loading="{loading}" decoding="async" />
                {shots}
              </span>
              <span class="line-title">{item.title}</span>
              {_price_html(item)}
            </summary>
            <div class="detail">
              {_gallery_html(item)}
              {desc}
              <p class="detail-foot">
                {ref}
                <a class="permalink" href="#{slug}">Link to this item</a>
              </p>
            </div>
          </details>
        </li>
        """


def _validate(items: list[Item], root: Path) -> None:
    missing = [
        path for item in items for path in item.image_paths if not (root / path).is_file()
    ]
    if missing:
        listed = '\n  '.join(path.as_posix() for path in missing)
        msg = f'Referenced images do not exist:\n  {listed}'
        raise FileNotFoundError(msg)


def _generate_html(items: list[Item], last_updated: datetime) -> str:
    section_config = [
        (ItemStatus.PAID, 'For Sale'),
        (ItemStatus.FREE, 'Free'),
        (ItemStatus.PENDING, 'Pending Pickup'),
    ]

    items_by_status = {status: [] for status in ItemStatus}
    for item in items:
        items_by_status[item.status].append(item)

    line_no = 0
    eager_budget = 3
    sections_html = []
    for status, section_title in section_config:
        status_items = items_by_status[status]
        if not status_items:
            continue

        lines_html = []
        for item in status_items:
            line_no += 1
            lines_html.append(_line_html(item, line_no, eager=line_no <= eager_budget))

        count = len(status_items)
        sections_html.append(f"""
      <section id="{status.value}">
        <h2 class="section-head">
          {section_title}
          <a class="section-anchor" href="#{status.value}" aria-label="Link to the {section_title} section">#</a>
          <span class="section-count label">{count} {"item" if count == 1 else "items"}</span>
        </h2>
        <ol class="manifest">
          {"".join(lines_html)}
        </ol>
      </section>
      """)

    return f"""<!doctype html>
<html lang="en">
{DIRECTION_CONTRACT}
{HEAD_HTML}
<body>
  <header class="masthead">
    <div class="wrap">
      <p class="label">East Polanco &middot; Ciudad de M&eacute;xico</p>
      <h1>Free &amp; For Sale</h1>
      <p class="standfirst">
        Board games, baby gear, and other things around the apartment we
        don't use anymore. Prices are roughly half of Amazon and I accept pesos
        or dollars, Venmo, PayPal, etc. Message me in the building WhatsApp
        group to ask questions and arrange a time.
      </p>
      <dl class="fields">
        <div>
          <dt class="label">Pickup</dt>
          <dd>East side of Polanco, near Liverpool</dd>
        </div>
        <div>
          <dt class="label">Updated</dt>
          <dd>{last_updated.strftime("%B %-d, %Y")}</dd>
        </div>
      </dl>
    </div>
  </header>

  <main class="wrap">
    {"".join(sections_html)}
  </main>
  {SCRIPT_HTML}
</body>
</html>
"""


def main() -> None:
    root = Path(__file__).parent
    items = [item for item in ITEMS if item.title != PLACEHOLDER_TITLE]
    _validate(items, root)
    skipped = len(ITEMS) - len(items)
    output_path = root / 'whatsapp-items.html'
    last_updated = datetime.now(UTC).astimezone()
    output_path.write_text(_generate_html(items, last_updated))
    print(f'Generated {output_path} ({len(items)} lines, {skipped} placeholder skipped)')


if __name__ == '__main__':
    main()
