"""Generate static HTML page for free items listing.

Color Palettes Considered from Color Hunt (https://colorhunt.co):

1. Calm & Natural (#364547, #7FA99B, #C8DBBB, #F7F7E8)
2. Soft & Approachable (#FFE6E6, #F7F5EB, #AACAA7, #8B9A8B)
3. Modern & Bold (#222831, #393E46, #00ADB5, #EEEEEE)
"""

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path


class ItemStatus(StrEnum):
    AVAILABLE = 'available'
    PENDING = 'pending'


@dataclass(frozen=True)
class Item:
    title: str
    image_path: Path
    status: ItemStatus
    link: str
    description: str = ''


ITEMS: list[Item] = [
    Item(
        title=title,
        image_path=Path('whatsapp-items') / image_name,
        status=ItemStatus(status),
        link=link,
        description=description,
    )
    for title, image_name, status, link, description in [
        (
            'Munchkin Secure Grip™ Changing Pad Rev 2.0',
            'Baby-Changing.jpeg',
            ItemStatus.AVAILABLE,
            'https://www.munchkin.com/secure-grip-changing-pad',
            'Clean with extra linens. We would keep this, but we needed a smaller one',
        ),
        (
            'MALMBÄCK IKEA Bathroom Shelf',
            'Bathroom-Shelf.jpeg',
            ItemStatus.AVAILABLE,
            'https://www.ikea.com/us/en/p/malmbaeck-display-shelf-white-20446236',
            'Display shelf, white, 23 5/8"',
        ),
        (
            'IKEA Bedroom Blackout Curtains',
            'Bedrom-Curtains.jpeg',
            ItemStatus.AVAILABLE,
            'https://www.ikea.com/us/en/p/vilborg-room-darkening-curtains-1-pair-beige-with-heading-tape-00297553',
            '',
        ),
        (
            'ARRIS SurfBoard SB6141 Modem',
            'Home-Modem.jpeg',
            ItemStatus.AVAILABLE,
            'https://www.amazon.com/ARRIS-SURFboard-SB6141-DOCSIS-Cable/dp/B00AJHDZSI',
            "I'm not sure if this will work with local providers, but if you're heading back to the US this modem is"
            ' older, but still good',
        ),
        (
            'Office Organizer Tray',
            'Home-Tray.jpeg',
            ItemStatus.AVAILABLE,
            '',
            '',
        ),
        (
            'More Organizer Trays',
            'home-more-trays.jpeg',
            ItemStatus.AVAILABLE,
            '',
            '',
        ),
        (
            'Framed World Map',
            'House-World-Map.jpeg',
            ItemStatus.AVAILABLE,
            '',
            "Note that the outside of the frame is slightly damaged from a fall, but isn't visible when mounted. The"
            ' glass and map are in good condition. The frame is from IKEA',
        ),
        (
            'Large Wooden Serving Bowl',
            'Kitchen-Bowl.jpeg',
            ItemStatus.AVAILABLE,
            '',
            'Made in Thailand from Lipper International',
        ),
        (
            'Over the Cabinet Lid Organizer (Bronze)',
            'Kitchen-Overdoor.jpeg',
            ItemStatus.AVAILABLE,
            'https://www.amazon.com/dp/B015EWKH2E?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_5',
            '5.25" L X 12.25" W X 19.25" H',
        ),
        (
            'Small Serving Tray',
            'Kitchen-Tray.jpeg',
            ItemStatus.AVAILABLE,
            '',
            'From Michel Design Works',
        ),
        (
            "Thousand Fell Men's Lace Up (Color Dune, 11.5 Men)",
            'Shoes.jpeg',
            ItemStatus.AVAILABLE,
            'https://www.thousandfell.com/products/mens-lace-up-sneaker-white',
            'These shoes are brand new and never worn. They are great shoes, but not my style',
        ),
        (
            'Scalpers Brown Leather Wallet',
            'Wallet-01-Flat.jpeg',  # "Wallet-01-Back.jpeg",
            ItemStatus.AVAILABLE,
            'https://en.ww.scalperscompany.com/products/61778-scmondit-free-wallet-aw2526-brown',
            'I received this as a gift, but I had already gotten a new wallet. $30 USD or best offer.'
            ' Made from 100% Cow Leather and never used and includes original tags if you would like to'
            ' give it as a gift',
        ),
    ]
]

HEAD_HTML = """
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Free Items</title>

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;500&display=swap"
  rel="stylesheet"
/>

<style>
  /* Color palette from Color Hunt - Calm & Natural theme
     https://colorhunt.co/palette/364547-7fa99b-c8dbbe-f7f7e8
     Primary: #364547 (dark teal), #7FA99B (sage green)
     Secondary: #C8DBBB (soft mint), #F7F7E8 (cream)
  */
  :root {
    --color-bg: #F7F7E8;
    --color-fg: #364547;
    --color-border: #C8DBBB;
    --color-card-bg: #ffffff;
    --color-available: #7FA99B;
    --color-pending: #C8DBBB;
    --color-pending-fg: #364547;
  }
  @media (prefers-color-scheme: dark) {
    body {
      --color-bg: #1e1e20;
      --color-fg: #C8DBBB;
      --color-border: #364547;
      --color-card-bg: #2a2a2c;
      --color-available: #7FA99B;
      --color-pending: #7FA99B;
      --color-pending-fg: #1e1e20;
    }
  }

  body {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: "Roboto", sans-serif;
    margin: 0;
    padding: 1rem;
  }

  #container {
    max-width: 1200px;
    margin: 0 auto;
  }

  h1 {
    text-align: center;
    font-size: 2.5rem;
    margin: 2rem 0;
    color: var(--color-fg);
  }

  #items-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
  }

  .item-card {
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1rem;
    background: var(--color-card-bg);
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .item-card[open] {
    grid-column: span 2;
    box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.15);
  }

  .item-card:hover {
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    transform: translateY(-2px);
  }

  .item-card[open]:hover {
    transform: none;
  }

  .item-card summary {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    cursor: pointer;
  }

  .item-card summary::-webkit-details-marker {
    display: none;
  }

  .item-card summary::marker {
    display: none;
  }

  .item-thumbnail {
    width: 100%;
    max-height: 250px;
    object-fit: cover;
    border-radius: 4px;
    transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .item-card[open] .item-thumbnail {
    display: none;
  }

  .item-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
    transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .item-card[open] summary .item-header {
    display: none;
  }

  .item-title {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 500;
    flex: 1;
  }

  .badge {
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.875rem;
    font-weight: 500;
    white-space: nowrap;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .badge-available {
    background: var(--color-available);
    color: white;
  }

  .badge-pending {
    background: var(--color-pending);
    color: var(--color-pending-fg);
  }

  .item-expanded {
    display: flex;
    gap: 1.5rem;
    margin-top: 1rem;
    animation: fadeInExpand 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  }

  @keyframes fadeInExpand {
    from {
      opacity: 0;
      transform: translateY(-20px) scale(0.95);
    }
    to {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
  }

  .item-full-image {
    flex: 1;
    max-width: 500px;
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 4px;
  }

  .item-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .item-header-expanded {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .item-description {
    line-height: 1.6;
    margin: 0;
  }

  #footer {
    text-align: center;
    color: var(--color-fg);
    opacity: 0.6;
    font-size: 0.875rem;
    padding: 2rem 0;
  }

  @media (max-width: 768px) {
    h1 {
      font-size: 2rem;
    }

    .item-card[open] {
      grid-column: span 1;
    }

    .item-expanded {
      flex-direction: column;
    }

    .item-full-image {
      max-width: 100%;
    }
  }

  @media (min-width: 769px) and (max-width: 900px) {
    /* On smaller desktops/tablets, allow single column span if needed */
    .item-card[open] {
      grid-column: span 1;
    }
  }
</style>
</head>
"""

# No JavaScript needed! The native `name` attribute on details elements
# provides exclusive accordion behavior in modern browsers (Firefox 130+, Chrome 120+, Safari 17.4+)
SCRIPT_HTML = ''


def _generate_html(items: list[Item], last_updated: datetime) -> str:
    status_badge_html = {
        ItemStatus.AVAILABLE: '<span class="badge badge-available">Available</span>',
        ItemStatus.PENDING: '<span class="badge badge-pending">Pending Pickup</span>',
    }

    items_html = []
    for item in items:
        desc_html = (
            f'<p class="item-description">{item.description}</p>'
            if item.description
            else ''
        )
        items_html.append(f"""
        <details class="item-card" name="free-items">
          <summary>
            <img src="{item.image_path.as_posix()}" alt="{item.title}" class="item-thumbnail" />
            <div class="item-header">
              <h3 class="item-title">{item.title}</h3>
              {status_badge_html[item.status]}
            </div>
          </summary>
          <div class="item-expanded">
            <img src="{item.image_path.as_posix()}" alt="{item.title}" class="item-full-image" />
            <div class="item-content">
              <div class="item-header-expanded">
                <h3 class="item-title">{item.title}</h3>
                {status_badge_html[item.status]}
              </div>
              {desc_html}
            </div>
          </div>
        </details>
        """)

    return f"""<!doctype html>
  <html lang="en">
  {HEAD_HTML}
  <body>
    <div id="container">
      <h1>Free Items</h1>
      <div id="items-grid">
{"".join(items_html)}
      </div>
      <div id="footer">
        Last updated: {last_updated.strftime("%B %d, %Y at %I:%M %p")}
      </div>
    </div>
    {SCRIPT_HTML}
  </body>
</html>
"""


def main() -> None:
    output_path = Path(__file__).parent / 'whatsapp-items.html'
    last_updated = datetime.now(UTC).astimezone()
    html_content = _generate_html(ITEMS, last_updated)
    output_path.write_text(html_content)
    print(f"Generated {output_path}")


if __name__ == '__main__':
    main()
