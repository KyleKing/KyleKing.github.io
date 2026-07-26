# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Recruiters, hiring managers, and prospective collaborators who arrive at kyleking.me to judge Kyle King's professional credibility before or during a conversation. They usually come from a profile link, a signature, or a search, already know the name, and want to confirm who he is and how to reach him in under a minute.

A second audience uses `whatsapp-items.html`: neighbours in the building's Free and For Sale WhatsApp chats in Polanco (Mexico City), browsing household, baby, and board game items Kyle and his family no longer use. They arrive from a chat link, almost always on a phone.

## Product Purpose

A personal website that establishes professional credibility and routes visitors to the right contact channel. Success is a visitor who leaves knowing what Kyle does, where he has worked, and how to reach him.

## Positioning

The site is the canonical, self-owned version of Kyle's professional identity, not a profile hosted inside someone else's platform.

## Operating Context

Static files served by GitHub Pages at kyleking.me, with Cloudflare as CDN, NameCheap for the domain, ImprovMX for email forwarding, and UptimeRobot for availability monitoring. Local development is `open index.html`; deployment is `git push`.

`whatsapp-items.html` is a build product of `generate_whatsapp.py`, which reads a hardcoded `ITEMS` list and photos under `whatsapp-items/`. A pre-commit hook regenerates the page whenever the script or the photo directory changes.

## Capabilities and Constraints

- Static HTML only. No build step, no bundler, no framework. Every page must open correctly from the filesystem
- `whatsapp-items.html` is generated output and is never hand-edited. All changes to it go through `generate_whatsapp.py`, which owns its markup and CSS. It is excluded from the prettier and trailing-whitespace pre-commit hooks
- Both pages support light and dark via `prefers-color-scheme` and must continue to
- Dependency-light and fast: the only external request today is a Google Fonts stylesheet. Icons are inlined as data-URI SVG masks
- Photographs are never published straight from the camera. `process_images.py` strips metadata from every source image, since GPS coordinates in a photo taken at home would publish that address, and builds the resized copies the items page serves
- The items page runs its own visual world and does not inherit DESIGN.md, which governs `index.html` only. See `.impeccable/surfaces/whatsapp-items-html.md`
- The items page carries no contact link. Publishing a phone number on a page open to the internet is not worth the convenience when the audience is already in the chat

## Brand Commitments

Existing name and identity: Kyle King. Contact surfaces are GitHub (github.com/KyleKing), LinkedIn (linkedin.com/in/kylemorganking), and email (dev.act.kyle@gmail.com).

## Evidence on Hand

Real biography, currently the full body copy of `index.html`: founding software engineer at Coverbase (procurement and TPRM); previously tech lead on multiple products at Parexel AI Labs (NLP and LLMs for pharmaceutical services); before that, robotic control software for medical instruments at Meso Scale Discovery. Eagle Scout. Prior work in a microfluidics lab, a Halobacterium genetics lab, and with animals at the Maryland Zoo in Baltimore. Masters in Computer Science from Georgia Tech, B.S. in Bioengineering from the University of Maryland.

Portrait photo at `IMG_0428.jpeg`. Item photos under `whatsapp-items/`.

No testimonials, case studies, metrics, press, project write-ups, or writing samples exist in this repository. Future work must not invent them.

## Product Principles

- Credibility comes from the real record. Every claim on the site traces to something Kyle actually did
- A visitor should reach a decision (who is this, how do I contact him) without scrolling for it
- Static and self-contained. Nothing on the site should require a toolchain to edit or a service to render
- Generated pages stay generated. The source of truth is the script, not the HTML
- Each surface owns its own visual world. The personal site and the items page share no palette, typeface, or component vocabulary, and neither borrows from the other
