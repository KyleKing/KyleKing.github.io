---
name: kyleking.me
description: A one-screen personal site where restraint is the credibility signal
colors:
  paper: '#f5f3ed'
  ink: '#1a1815'
  night: '#17171a'
  ash: '#b9b9be'
  fountain-ink: '#3a5a8c'
  fountain-ink-pale: '#93aede'
typography:
  display:
    fontFamily: Newsreader, Georgia, 'Times New Roman', serif
    fontSize: clamp(2.5rem, 9vw, 3.5rem)
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.015em
  body:
    fontFamily: Newsreader, Georgia, 'Times New Roman', serif
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: normal
  label:
    fontFamily: Newsreader, Georgia, 'Times New Roman', serif
    fontSize: 1.875rem
    fontWeight: 400
    lineHeight: 2.25rem
    letterSpacing: normal
rounded:
  none: '0'
  full: 50%
spacing:
  tight: 0.75rem
  block: 1.25rem
  gutter: 5%
  section: 5rem
components:
  portrait:
    rounded: '{rounded.full}'
    height: 15rem
    width: 15rem
  icon-link:
    textColor: inherit
    height: 1.2em
    width: 1.2em
  icon-link-hover:
    textColor: inherit
    height: 1.2em
    width: 1.2em
  text-link:
    textColor: '{colors.fountain-ink}'
    typography: '{typography.body}'
---

# Design System: kyleking.me

## Overview

**Creative North Star: "The Quiet Résumé"**

The page reads like a printed page rather than a web application. It is paper-colored, low in contrast, and unhurried, and it asks nothing of the visitor except to read two short paragraphs and pick a way to get in touch. A recruiter arriving from a profile link should form a judgment in under a minute, and the restraint of the surface is what earns that judgment. Loud design on a personal page reads as compensation, so this page declines to compensate.

Everything sits in one vertically centered column against a full-viewport field of warm off-white. There is no navigation, no scroll narrative, and no second destination, because there is no second page. Depth is absent by construction: no shadows, no borders, no cards, no dividers. Separation comes from generous vertical air (`5rem` spacers opening and closing the column) and from the contrast between the one circular photograph and the flat ground it sits on.

Color is nearly absent. The palette is a warm paper and a warm near-black in light mode, mirrored to a cool charcoal and a cool ash in dark mode, with a single fountain-pen blue reserved for links. Type is Newsreader at one weight, with optical sizing on, so the name and the body copy are cut by the same hand at different sizes. The page is static HTML with inlined SVG icon masks and one font request, and that economy is a standing constraint rather than a temporary state.

**Key Characteristics:**

- One centered column, one viewport, no navigation
- Warm paper and warm ink by day, cool charcoal and cool ash by night
- A single serif at a single weight, with optical sizing carrying the size range
- Uniformly flat: no shadow, no border, no card, no divider
- A single circular portrait as the only geometric event
- Static HTML with inlined icons and no build step

## Colors

A paper-and-ink palette with one reserved accent, mirrored across light and dark schemes at deliberately moderate contrast.

### Primary

- **Fountain Ink** (`#3a5a8c`): every link in light mode, and the focus ring on the contact icons. A muted blue that reads as pen on paper rather than as a web link. 6.3:1 on Warm Paper
- **Pale Fountain Ink** (`#93aede`): the same role in dark mode. 8.0:1 on Charcoal Night

### Neutral

- **Warm Paper** (`#f5f3ed`): the light-mode page ground, filling the entire viewport. Slightly warm and slightly off-white, which reads as stock rather than as a screen
- **Warm Near-Black** (`#1a1815`): all light-mode text and, through `currentColor`, the fill of the masked contact icons. Warmed off pure black so it sits on the paper instead of cutting into it. 16.0:1 on Warm Paper
- **Charcoal Night** (`#17171a`): the dark-mode page ground. Faintly cool, which sets it against Warm Paper rather than reading as its plain inverse
- **Cool Ash** (`#b9b9be`): dark-mode text and icon fill. Deliberately short of white so the dark mode stays as low-contrast as the light mode. 9.2:1 on Charcoal Night

### Named Rules

**The Two-Tone Rule.** Any screen resolves to one ground and one ink. The fountain blue is the single exception, and it is reserved for links. A fourth color needs a reason that survives being stated out loud, and "it looked bare" is not one.

**The Mirror Rule.** Dark mode is a scheme of equal standing, not a filter over the light one. Both grounds are chosen for their own temperature (`#f5f3ed` warm, `#17171a` cool), the inks follow their ground's temperature, and both schemes define the accent explicitly.

## Typography

**Display Font:** Newsreader (with Georgia, `'Times New Roman'`, serif fallback) **Body Font:** Newsreader, same stack

**Character:** One serif at weight 400 across the entire page, loaded as a variable font with `font-optical-sizing: auto`. Newsreader is cut for reading on screen, so the body copy stays even and unfussy at `1.125rem`, while optical sizing thins the strokes and tightens the spacing at display size on its own. The face carries the printed-page reference the north star asks for without any period-costume mannerism.

### Hierarchy

- **Display** (400, `clamp(2.5rem, 9vw, 3.5rem)`, line-height 1.05, tracking `-0.015em`): the name, and the only element permitted at this size. The clamp lets it shrink on narrow screens with no breakpoint; the tight line-height and slight negative tracking keep it a compact mark rather than a headline
- **Body** (400, `1.125rem`, line-height 1.7): the biography paragraphs, left aligned, held to a `38rem` measure (about 61 characters). The open line-height is what makes a serif at this size restful
- **Label** (400, `1.875rem`, line-height `2.25rem`): the contact icon row. The size is a glyph scale rather than a text scale

### Named Rules

**The One Weight Rule.** The page uses a single family at weight 400. Hierarchy is built from size, optical sizing, and vertical air. No bold, no italic, no uppercase, no letter-spacing tricks beyond the display's `-0.015em`.

**The Two Sizes Rule.** Display and Body are the whole text scale. Introducing a third text size means the page has grown a section it probably should not have.

## Layout

A single flex column centered both ways in a full-viewport container (`height: 100dvh` with a `100vh` fallback, `align-items: center`, `justify-content: center`). Content is capped at `38rem` and gets a `5%` gutter on each side, so the measure narrows smoothly on small screens with no breakpoint. The column carries `min-width: 0` and `min-height: 0` so the portrait is never squeezed by flex sizing on mobile.

Portrait, name, and icon row are centered; the biography paragraphs are left aligned inside that centered column. Centered running text at this length is hard to track line to line, and the ragged right edge is what makes the block read as a page rather than a poster.

Vertical rhythm comes from four values: `5rem` spacers opening and closing the column, `1.75rem` above the name and `1.5rem` below it, `1.25rem` between paragraphs, and `0.75rem` between contact icons. More space sits above the name than below it, so it binds to the paragraphs it introduces.

There are no size breakpoints and no grid. Responsive behavior comes from the `clamp()` on the display size, the `38rem` cap, and the percentage gutter. The only media query in the file is `prefers-color-scheme`.

## Elevation & Depth

The system is entirely flat. There are no shadows, no borders, no background layers, and no dividers anywhere on the page. Every element sits directly on the single ground color.

Depth, where it registers at all, comes from two sources: the circular portrait reading as an object against a flat field, and the contact icons sitting at 55% opacity so they recede behind the text until pointed at. Opacity is this system's only depth cue.

### Named Rules

**The No Surface Rule.** Nothing gets a background, a border, or a shadow. If content needs separating, separate it with space.

## Shapes

The page has exactly one shape event: the portrait, a perfect circle (`border-radius: 50%`) at `15rem` square with `object-fit: cover`. Everything else is unshaped text and masked icon glyphs with no container, so no radius scale applies to them.

Icons are rendered as CSS masks over `currentColor` rather than as images, which keeps them tied to the text color in both schemes and adds no network request.

## Components

### Contact Icon Link

The signature and only interactive element. A `1.2em` square anchor with no label, no background, and no border, drawn by masking `currentColor` through an inlined Carbon SVG data URI.

- **Shape:** unrounded square bounds (`rounded.none`); the glyph supplies its own silhouette
- **Color:** `background-color: currentColor` under a mask, so the icon always matches the surrounding ink in both schemes
- **Rest:** `opacity: 0.55`. Recessive enough that the row does not compete with the name, and above the 3:1 floor for a non-text control in both schemes (3.8:1 light, 3.6:1 dark)
- **Hover:** `opacity: 0.95` over `400ms` on `cubic-bezier(0.4, 0, 0.2, 1)`. The slow, wide-eased fade is the page's only motion and reads as a considered response rather than a snap
- **Focus:** the same opacity lift plus a `2px` Fountain Ink outline at `4px` offset. A masked anchor has no visible box of its own, so focus must draw one
- **Spacing:** `0.75rem` gap, so the three icons read as one group without touching

### Text Link

Fountain Ink in both schemes, underlined at `1px` with a `0.15em` underline offset so descenders clear the rule. Links inherit the body size and weight; color and the underline carry the affordance.

### Portrait

A `15rem` circle with `object-fit: cover`, sitting above the name. It is the only image, the only curve, and the only saturated area on the page, and it does the work a logo would do elsewhere.

## Do's and Don'ts

### Do:

- **Do** keep the entire page inside one centered column at a `38rem` cap with a `5%` gutter
- **Do** resolve every screen to one ground and one ink, reserving the fountain blue for links, per The Two-Tone Rule
- **Do** left align running text inside the centered column; center only the portrait, the name, and the icon row
- **Do** build hierarchy from size, optical sizing, and vertical air, using the `5rem` / `1.75rem` / `1.25rem` / `0.75rem` rhythm already in place
- **Do** define both color schemes deliberately, including the accent; dark mode is not a post-processing pass
- **Do** inline icons as SVG data URI masks over `currentColor`, adding no network request and no icon dependency
- **Do** give every interactive element a visible `:focus-visible` treatment, since nothing here has a box of its own to shift
- **Do** keep new work editable as plain static HTML that opens from the filesystem

### Don't:

- **Don't** add a shadow, border, card, or divider. Separation is space, per The No Surface Rule
- **Don't** introduce a second font family, a second weight, or bold, italic, and uppercase treatments
- **Don't** spend Fountain Ink on anything but links and focus rings. It is not a heading color, a button fill, or a hover state
- **Don't** add a navigation bar, header chrome, or footer. There is no second page, and chrome implying one would be a lie
- **Don't** import a CSS framework, a build step, or an icon package
- **Don't** borrow the marketing landing page vocabulary: gradient hero, feature grid, testimonial row, oversized CTA
- **Don't** borrow the developer portfolio template vocabulary: terminal green, monospace body text, typing animations, contribution graphs
- **Don't** borrow the maximal personal brand vocabulary: full-bleed photography, scroll-jacking, display type at hero scale, motion on every element
- **Don't** treat `whatsapp-items.html` as part of this system. It is a temporary surface for one move, running its own throwaway sage palette (`#7fa99b`, `#c8dbbb`, `#f7f7e8`) with cards, badges, and shadows that this system rejects. Nothing here inherits from it, and it is generated only by `generate_whatsapp.py`
