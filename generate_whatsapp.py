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
    AVAILABLE = "available"
    PENDING = "pending"
    PAID = "paid"


@dataclass(frozen=True)
class Item:
    title: str
    image_paths: list[Path]
    status: ItemStatus
    link: str
    description: str
    price: str = ""


ITEMS: list[Item] = [
    Item(
        title=title,
        image_paths=[Path("whatsapp-items") / img for img in image_names],
        status=ItemStatus(status),
        link=link,
        description=description,
        price=price,
    )
    for title, image_names, status, link, description, price in [
        (
            "Scalpers Brown Leather Wallet",
            ("Wallet-01-Flat.jpeg", "Wallet-04-Back.jpeg"),
            ItemStatus.PAID,
            "https://en.ww.scalperscompany.com/products/61778-scmondit-free-wallet-aw2526-brown",
            "I received this as a gift, but I had already gotten a new wallet."
            " Made from 100% Cow Leather and never used and includes original tags if you would like to"
            " give it as a gift",
            "$30 USD or best offer",
        ),
        (
            "Thousand Fell Men's Lace Up (Color Dune, 11.5 Men)",
            ("Shoes.jpeg",),
            ItemStatus.PAID,
            "https://www.thousandfell.com/products/mens-lace-up-sneaker-white",
            "These shoes are great and brand new and never worn, but they aren't my style",
            "$20 USD or best offer",
        ),
        (
            "Munchkin Secure Grip™ Changing Pad Rev 2.0",
            ("Baby-Changing.jpeg",),
            ItemStatus.AVAILABLE,
            "https://www.munchkin.com/secure-grip-changing-pad",
            "Clean with extra linens. We would keep this, but we needed a smaller one",
            "",
        ),
        (
            "MALMBÄCK IKEA Bathroom Shelf",
            ("Bathroom-Shelf.jpeg",),
            ItemStatus.AVAILABLE,
            "https://www.ikea.com/us/en/p/malmbaeck-display-shelf-white-20446236",
            'Display shelf, white, 23 5/8"',
            "",
        ),
        (
            "IKEA Bedroom Blackout Curtains",
            ("Bedrom-Curtains.jpeg",),
            ItemStatus.AVAILABLE,
            "https://www.ikea.com/us/en/p/vilborg-room-darkening-curtains-1-pair-beige-with-heading-tape-00297553",
            "",
            "",
        ),
        (
            "ARRIS SurfBoard SB6141 Modem",
            ("Home-Modem.jpeg",),
            ItemStatus.AVAILABLE,
            "https://www.amazon.com/ARRIS-SURFboard-SB6141-DOCSIS-Cable/dp/B00AJHDZSI",
            "We can't use this modem with Telmex because it requires a regular Ethernet hookup, but it may"
            " work with other providers. While older, this works well and I would keep it if we had a use for it",
            "",
        ),
        (
            "Organizer Trays",
            ("Home-Tray.jpeg", "home-more-trays.jpeg"),
            ItemStatus.AVAILABLE,
            "",
            "",
            "",
        ),
        (
            "Framed World Map",
            ("House-World-Map.jpeg",),
            ItemStatus.AVAILABLE,
            "",
            "While the IKEA frame has minor exterior damage from a fall, it is not visible when mounted. The glass and"
            " map are in good condition",
            "",
        ),
        (
            "Large Wooden Serving Bowl",
            ("Kitchen-Bowl.jpeg",),
            ItemStatus.AVAILABLE,
            "",
            "Made in Thailand from Lipper International",
            "",
        ),
        (
            "Over the Cabinet Lid Organizer (Bronze)",
            ("Kitchen-Overdoor.jpeg",),
            ItemStatus.AVAILABLE,
            "https://www.amazon.com/dp/B015EWKH2E?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_5",
            '5.25" L X 12.25" W X 19.25" H',
            "",
        ),
        (
            "Small Serving Tray",
            ("Kitchen-Tray.jpeg",),
            ItemStatus.AVAILABLE,
            "",
            "From Michel Design Works",
            "",
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
    --color-paid: #E8A87C;
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
      --color-paid: #E8A87C;
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

  .items-section {
    margin-bottom: 3rem;
  }

  .section-title {
    font-size: 1.75rem;
    margin: 2rem 0 1.5rem 0;
    color: var(--color-fg);
  }

  .items-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
  }

  .item-card {
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1rem;
    background: var(--color-card-bg);
    overflow: visible;
    transition: all 0.2s ease;
    position: relative;
  }

  .item-card[open] {
    grid-column: span 2;
    box-shadow: 0 6px 12px -2px rgb(0 0 0 / 0.15);
  }

  .item-card:hover:not([open]) {
    box-shadow: 0 2px 4px -1px rgb(0 0 0 / 0.1);
    transform: translateY(-2px);
    border-color: var(--color-available);
  }

  .item-card summary {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    cursor: pointer;
    position: relative;
  }

  .item-card summary::after {
    content: "▼ Click to expand";
    position: absolute;
    bottom: -0.5rem;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.75rem;
    color: var(--color-available);
    opacity: 0.7;
    transition: all 0.2s ease;
    padding: 0.5rem 1rem;
    margin: -0.75rem -1rem;
  }

  .item-card[open] summary::after {
    content: "";
  }

  .item-card summary::-webkit-details-marker {
    display: none;
  }

  .item-card summary::marker {
    display: none;
  }

  .close-button {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    width: 2.5rem;
    height: 2.5rem;
    background: var(--color-available);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
    padding: 0;
    transition: opacity 0.2s ease;
  }

  .close-button::before {
    content: "✕";
    color: white;
    font-size: 1.25rem;
    font-weight: bold;
  }

  .item-card[open]:not(:hover) .close-button {
    opacity: 0.5;
  }

  .item-card[open] .close-button:hover {
    opacity: 1;
  }

  .item-thumbnail-container {
    width: 100%;
    height: 200px;
    border-radius: 4px;
    overflow: hidden;
    position: relative;
  }

  .item-thumbnail-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: opacity 0.2s ease;
  }

  .image-count {
    position: absolute;
    bottom: 0.5rem;
    right: 0.5rem;
    background: rgba(0, 0, 0, 0.6);
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 500;
  }

  .item-card[open] .item-thumbnail-container {
    display: none;
  }

  .item-header {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    min-height: 3rem;
    padding-bottom: 0;
  }

  .item-header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
  }

  .item-price-closed {
    font-size: 1rem;
    font-weight: 500;
    color: var(--color-paid);
    margin: 0;
  }

  .item-card[open] summary .item-header {
    display: none;
  }

  .item-title {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 500;
    flex: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .item-card[open] .item-title {
    -webkit-line-clamp: unset;
    overflow: visible;
  }

  .badge {
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
    font-size: 0.875rem;
    font-weight: 500;
    white-space: nowrap;
  }

  .badge-available {
    background: var(--color-available);
    color: white;
  }

  .badge-pending {
    background: var(--color-pending);
    color: var(--color-pending-fg);
  }

  .badge-paid {
    background: var(--color-paid);
    color: white;
  }

  .item-expanded {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1rem;
    animation: fadeIn 0.3s ease;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(-10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .item-gallery {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: flex-start;
  }

  .item-gallery img {
    width: calc(50% - 0.25rem);
    height: auto;
    max-height: 300px;
    object-fit: cover;
    border-radius: 4px;
    flex-grow: 1;
  }

  .item-gallery img:only-child {
    width: 100%;
  }

  .item-content {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .item-header-expanded {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .item-price {
    font-size: 1.25rem;
    font-weight: 500;
    color: var(--color-paid);
    margin: 0 0 0.5rem 0;
  }

  .item-description {
    line-height: 1.6;
    margin: 0;
  }

  .item-link {
    display: block;
    margin: 0.5rem auto 0;
    padding: 0.75rem 1.5rem;
    background-color: var(--color-available);
    color: white;
    text-decoration: none;
    border-radius: 6px;
    font-size: 0.9rem;
    font-weight: 500;
    transition: opacity 0.2s ease;
    text-align: center;
    width: fit-content;
  }

  .item-link:hover {
    opacity: 0.9;
  }

  @media (max-width: 768px) {
    h1 {
      font-size: 2rem;
    }

    .item-gallery img {
      max-height: 300px;
      width: 100%;
    }

    .item-card summary::after {
      font-size: 0.7rem;
    }
  }
</style>
</head>
"""

# No JavaScript needed! The native `name` attribute on details elements
# provides exclusive accordion behavior in modern browsers (Firefox 130+, Chrome 120+, Safari 17.4+)
SCRIPT_HTML = """<script>
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const openCard = document.querySelector('details[open]');
    if (openCard) {
      openCard.open = false;
    }
  }
});
</script>"""


def _generate_html(items: list[Item], last_updated: datetime) -> str:
    status_badge_html = {
        ItemStatus.AVAILABLE: '<span class="badge badge-available">Available</span>',
        ItemStatus.PENDING: '<span class="badge badge-pending">Pending Pickup</span>',
        ItemStatus.PAID: '<span class="badge badge-paid">Paid</span>',
    }

    section_config = [
        (ItemStatus.PAID, "Paid Items"),
        (ItemStatus.AVAILABLE, "Free Items"),
        (ItemStatus.PENDING, "Pending Pickup"),
    ]

    items_by_status = {status: [] for status in ItemStatus}
    for item in items:
        items_by_status[item.status].append(item)

    sections_html = []
    for status, section_title in section_config:
        status_items = items_by_status[status]
        if not status_items:
            continue

        items_html = []
        for item in status_items:
            desc_html = (
                f'<p class="item-description">{item.description}</p>'
                if item.description
                else ""
            )
            link_html = (
                f'<a href="{item.link}" target="_blank" class="item-link">View Product</a>'
                if item.link
                else ""
            )
            price_html = (
                f'<p class="item-price">{item.price}</p>'
                if item.price and item.status == ItemStatus.PAID
                else ""
            )
            price_closed_html = (
                f'<p class="item-price-closed">{item.price}</p>'
                if item.price and item.status == ItemStatus.PAID
                else ""
            )
            # Generate image gallery
            images_html = []
            for img_path in item.image_paths:
                images_html.append(
                    f'<img src="{img_path.as_posix()}" alt="{item.title}" class="item-image" />'
                )

            image_count_html = (
                f'<span class="image-count">{len(images_html)}</span>'
                if len(images_html) > 1
                else ""
            )

            items_html.append(f"""
        <details class="item-card" name="free-items">
          <summary>
            <div class="item-thumbnail-container">
              {images_html[0]}
              {image_count_html}
            </div>
            <div class="item-header">
              <div class="item-header-row">
                <h3 class="item-title">{item.title}</h3>
                {status_badge_html[item.status]}
              </div>
              {price_closed_html}
            </div>
          </summary>
          <button class="close-button" aria-label="Close" onclick="this.closest('details').open = false;"></button>
          <div class="item-expanded">
            <div class="item-gallery">
              {"".join(images_html)}
            </div>
            <div class="item-content">
              <div class="item-header-expanded">
                <h3 class="item-title">{item.title}</h3>
                {status_badge_html[item.status]}
              </div>
              {price_html}
              {desc_html}
              {link_html}
            </div>
          </div>
        </details>
        """)

        sections_html.append(f"""
      <section class="items-section">
        <h2 class="section-title">{section_title}</h2>
        <div class="items-grid">
          {"".join(items_html)}
        </div>
      </section>
      """)

    return f"""<!doctype html>
  <html lang="en">
  {HEAD_HTML}
  <body>
    <div id="container">
      <h1>Free and Paid Items</h1>
      <p style="max-width: 600px; margin-right: auto; margin-left: auto;">All items available for pickup on the East Side of Polanco. Message me on WhatsApp to arrange a time. (Last updated: {last_updated.strftime("%B %d, %Y at %I:%M %p")})</p>
      {"".join(sections_html)}
    </div>
    {SCRIPT_HTML}
  </body>
</html>
"""


def main() -> None:
    output_path = Path(__file__).parent / "whatsapp-items.html"
    last_updated = datetime.now(UTC).astimezone()
    html_content = _generate_html(ITEMS, last_updated)
    output_path.write_text(html_content)
    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()
