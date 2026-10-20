---
name: Dialectic Skills
description: Project page for dia, seven reasoning-and-review skills in one plugin, drawn from one motif, two overlapping circles and the amber lens where they meet.
colors:
  sky: "#cbe4f2"
  sky-tone: "#b6d7ea"
  sand: "#f1e3b5"
  sand-tone: "#e7d49a"
  ink: "#0a0a0a"
  paper: "#f2f2f2"
  muted: "#3c5866"
  accent: "#f59e0b"
  accent-strong: "#e08a00"
  accent-ink: "#0a0a0a"
  blue-1: "#0e2a3a"
  blue-2: "#1b4660"
  blue-3: "#2c6688"
  blue-4: "#6fa3c3"
  blue-5: "#a3cbe2"
typography:
  display:
    fontFamily: "Libre Franklin, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.75rem, 0.6rem + 9vw, 6.75rem)"
    fontWeight: 700
    lineHeight: 0.92
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Libre Franklin, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 1.3rem + 3.2vw, 4rem)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Libre Franklin, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem)"
    fontWeight: 700
    lineHeight: 1.55
    letterSpacing: "-0.01em"
  lead:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(1.375rem, 1rem + 1.1vw, 1.875rem)"
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(0.8125rem, 0.79rem + 0.1vw, 0.875rem)"
    fontWeight: 400
    lineHeight: 1.45
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "0.86em"
    fontWeight: 400
rounded:
  panel: "28px"
  pill: "999px"
  circle: "50%"
spacing:
  margin: "clamp(1rem, 2.2vw, 2rem)"
  gutter: "clamp(1rem, 2vw, 2rem)"
  pad: "clamp(3.5rem, 6vw, 5.5rem)"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "0 1.6rem"
    height: "3.25rem"
  button-primary-hover:
    backgroundColor: "{colors.accent-strong}"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "0 1.6rem"
    height: "3.25rem"
  button-ink-hover:
    backgroundColor: "{colors.blue-1}"
  button-tone:
    backgroundColor: "{colors.sky-tone}"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "0 1.6rem"
    height: "3.25rem"
  button-tone-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  button-small:
    rounded: "{rounded.pill}"
    padding: "0 1.25rem"
    height: "2.75rem"
  surface-switch:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.title}"
    height: "3.75rem"
  surface-switch-tab:
    textColor: "{colors.blue-5}"
    rounded: "{rounded.pill}"
    padding: "0 0.9rem"
    height: "2.75rem"
  surface-switch-tab-active:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
  start-code-chip:
    backgroundColor: "{colors.sky-tone}"
    textColor: "{colors.ink}"
    typography: "{typography.code}"
    rounded: "{rounded.pill}"
    padding: "0.2em 0.7em"
  prompt-panel:
    backgroundColor: "{colors.sky-tone}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.panel}"
    padding: "1.1rem 1.4rem"
  question-tile:
    backgroundColor: "{colors.sky-tone}"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    rounded: "{rounded.panel}"
    padding: "1.1rem 4.5rem 1.1rem 1.6rem"
  question-tile-open:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
  install-stage:
    backgroundColor: "{colors.blue-1}"
    textColor: "{colors.paper}"
    padding: "1.5rem 2rem 2.25rem"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
---

# Design System: Dialectic Skills

## Overview

**Creative North Star: "Two Voices and the Lens"**

The whole page is drawn from one shape: dia's own mark, two overlapping circles (you and the assistant) and the amber lens where they meet. That shape is the hero, the frame of every picture, the speaker dot beside every turn of a session, the round end of every button and the mark built large in the footer. Nothing else on the page is decorative. If a new surface needs an accent, it borrows from the motif (a circle, a pill, the amber lens) rather than adding a new device.

The ground is two pale, flat fields, sky and sand, that alternate section by section and plate by plate, so the page reads as a sequence of plates in a printed edition. Pictures are public-domain artworks and documents from the history of argument (Socrates, Plato manuscripts, Euclid, Diogenes), always in greyscale inside the left circle, with the amber lens laid over them in multiply. Ink is near-black, never pure black on pure white; text is a serif set at reading length, headings a heavy grotesque.

Density is generous and editorial: one idea per screen, long real examples shown in full, no cards-in-grids. Motion is a single vocabulary of masked rises and circles sliding into overlap, and it disappears entirely under reduced motion.

**Key Characteristics:**
- One motif: two circles and an amber lens, repeated at every scale from a 0.6rem dot to a full-viewport hero.
- Flat colour fields (sky, sand, ink); no shadows, no gradients, no borders.
- Libre Franklin 700 for every heading and control; Source Serif 4 for all reading text.
- Monospace appears only on commands and code.
- Real material only: real shortened sessions, credited public-domain pictures, no invented proof.

## Colors

A pale sky-and-sand ground carried by near-black ink, with the logo's amber as the single accent and a five-step blue ramp reserved for the install stages.

### Primary
- **Lens Amber** (accent): the lens of the dia mark. Fills the primary button, the active surface tab, the open question tile, the "wants" dots, text selection and the lens shape over every picture. Ink text sits on it (accent-ink), never the reverse.
- **Burnt Amber** (accent-strong): hover state of amber buttons and the hover underline colour of plain links.

### Secondary
- **Stage Blues** (blue-1 to blue-5): a dark-to-light ramp from deep harbour blue to pale air. In order, they are the grounds of the five install stages (Claude Code, Codex, claude.ai and desktop, Claude mobile, ChatGPT); the first three carry paper text, the last two ink text. Single steps reappear in small roles: blue-1 for ink-button hover, blue-3 for the "You" speaker dot and the row dots in "Start a skill", blue-5 for inactive tabs in the ink switch bar.

### Neutral
- **Sky** (sky): the default page ground and the hero; also the theme colour.
- **Sky Tone** (sky-tone): a slightly deeper sky for panels sitting on sky: prompt boxes, code chips, question tiles, tone buttons, the grey backing behind pictures.
- **Sand** (sand): the alternate field, swapped in by sections and plates that take the sand ground; also the left circle of the mark.
- **Sand Tone** (sand-tone): the panel tone on sand fields.
- **Ink** (ink): text, the sticky switch bar, the footer, the right circle of the hero pair, ink buttons.
- **Paper** (paper): text on ink and on the dark stages. Never used as a page ground.
- **Slate Muted** (muted): captions, secondary notes, inactive surface tabs, group labels (5.7:1 on sky, 5.9:1 on sand).

### Named Rules
**The Paired Field Rule.** A section's ground is sky or sand, and its panel tone and second circle follow from it: on sky the tone is sky-tone and the second circle is sand; on sand the tone is sand-tone and the second circle is sky. Change the field, and the pairing changes with it; never mix a sand tone onto a sky field.

**The Amber Is a Fill Rule.** Amber is used as a filled shape (lens, dot, pill, open tile) with ink on top. It is never text colour on sky or sand (1.6:1).

**The Stage Order Rule.** The five blues are one ordered ramp for the five install stages, darkest first. Do not reuse the ramp as a general categorical palette.

## Typography

**Display Font:** Libre Franklin 700 (with Helvetica Neue, Arial)
**Body Font:** Source Serif 4, 400 to 600, with italic (with Georgia, Times New Roman)
**Label/Mono Font:** system monospace (ui-monospace, SFMono-Regular, Menlo, Consolas), for commands and code only

**Character:** A heavy, tightly tracked grotesque that talks like a poster against a calm book serif that reads like a printed dialogue. Both are self-hosted woff2 files under the SIL Open Font License.

### Hierarchy
- **Display** (700, clamp 2.75rem to 6.75rem, line-height 0.92, -0.035em, uppercase): the hero title and the footer word mark only. In the desktop hero it is further capped so two lines fit the left half.
- **Headline** (700, clamp 2rem to 4rem, line-height 1.02, -0.03em): section titles and skill names on each plate.
- **Title** (700, body size, -0.01em): navigation, buttons, surface tabs, question summaries, speaker names, definition terms in skill output, the bold run-in titles of the intro facts.
- **Lead** (400 serif, clamp 1.375rem to 1.875rem, line-height 1.3): the hero lead, the intro statement, the one-line promise under each skill name, install stage names.
- **Body** (400 serif, clamp 1.0625rem to 1.1875rem, line-height 1.55): all reading text, capped at 64ch; strong runs are 600.
- **Small** (400 serif, clamp 0.8125rem to 0.875rem, line-height 1.45): picture captions (46ch) and the footer credits.
- **Code** (monospace, 0.86em of the surrounding text): skill names, start commands, install commands, flags.

### Named Rules
**The Two Families Rule.** Headings and controls are Libre Franklin 700; everything read is Source Serif 4. No third family, no other weights of the display face.

**The Mono Means Type-This Rule.** Monospace marks only something the reader types or copies: commands, skill names, flags. Example prompts in plain language are set in the serif even inside a prompt panel, because they are sentences, not code.

## Layout

Full-bleed colour fields, each padded by the page margin (clamp 1rem to 2rem) with vertical section padding (clamp 3.5rem to 5.5rem). Inside, a 12-column grid with a fluid gutter (clamp 1rem to 2rem) sets split compositions: heading in columns 1 to 5 or 1 to 4, content from column 7 or 5 to the end.

- **Hero:** a full-height viewport; copy in the left half, the two-circle pair anchored to the right edge, sized from the viewport (radius min(40svh, 27vw)) and cropped by it.
- **Skill plates:** seven full-width plates, each two equal columns, at least 88svh tall, alternating sand and sky and alternating which side holds the picture. The picture column is sticky while the text scrolls.
- **Install:** five stages in one rounded panel; on wide screens a horizontal accordion (open stage 60% wide, closed stages show a vertical label), below 900px a vertical accordion.
- **Questions:** sticky heading on the left, accordion of tiles on the right.
- **Breakpoints:** 900px (splits collapse to one column; plates reorder to name, lead, picture, then text; picture shrinks to 64% and alternates left and right) and 600px (picture 72%, speaker names stack above turns, secondary nav link hidden).

Measures: body 64ch, captions 46ch, question answers 52ch, plate text 42rem.

## Elevation & Depth

The system is flat. There are no shadows anywhere. Depth comes from three things only: tonal steps within a field (sky to sky-tone, sand to sand-tone), the overlap of the two circles with the amber lens multiplied over the picture, and stacking order (the sticky ink switch bar passes over the plates).

### Named Rules
**The Flat Plate Rule.** Surfaces sit flat on their field. To separate a panel, step the tone; never add a shadow, border or gradient.

## Shapes

Every shape is a circle or derives from one.

- **Circles** (50%): picture frames, the speaker and list dots (0.6rem, 0.75rem and 1rem), inline thumbnails in the intro statement (1.4em, sitting on the line).
- **Pills** (999px): every button, the surface tabs, the native select in the phone switch, the start-command chips.
- **Panels** (28px): prompt boxes, install command boxes, question tiles, the install stage group. The only non-circular corner on the page.
- **The pair:** two circles on a 3:2 box overlapping by a third (hero, film, footer, wordmark), or on a square box overlapping on the diagonal (skill plates, mirrored on alternate plates). The lens is an SVG path filled with amber in multiply blend.

The open/close indicator in question tiles is drawn with two short CSS bars (a plus that turns into a minus), not a glyph or icon font.

## Components

### Buttons
Round, heavy and quiet: a pill of colour with display-face text.
- **Shape:** full pill (999px); 3.25rem tall, 2.75rem for the small size.
- **Primary (amber):** "Install dia" in the hero, the switch bar and the footer. Ink text on amber.
- **Ink:** "Copy the prompt" on each plate. Paper on ink; hover to blue-1.
- **Tone:** "Full guide" and the film toggle. Ink on the field's tone; hover inverts to paper on ink.
- **Press:** scales to 0.96 over 140ms. Hover colour changes only on fine pointers.
- **Copy (install):** a small pill in the stage's ink colour with the stage colour as text, beside each command; wraps below the command when the line is too short.

### Links
Navigation and footer links carry a transparent underline that appears on hover. Plain inline links keep a thin underline (0.07em, offset 0.2em) that turns burnt amber on hover.

### Surface Switch ("Where do you use it?")
The page's live control and its signature component. A sticky ink bar at the top of the skills section, present only when JavaScript runs. On wide screens: the label "Where do you use it?", five pill tabs (inactive blue-5 text, active amber pill with ink text) and a small amber Install button. Below 900px the tabs become a native select styled as an amber pill with an ink chevron, prefixed "Use on". Choosing a surface rewrites every skill's start command and copied prompt, and opens that surface's install stage; the choice persists in local storage.

### Surface tabs on plates
Display-face labels with a small dot before them: tone dot, scaled to 0.75, when off; full-size amber dot and ink text when on.

### Skill plate
A full-width field with the diagonal pair and a caption on one side and, on the other: headline skill name, lead promise, body paragraph, the start line (with a pill code chip and a muted note), a prompt panel, then a real shortened session or output, then an ink and a tone button.

### Session transcript
Each turn is a two-column row: speaker name in the display face with a circle before it (ink for Assistant, blue-3 for You), then the serif turn. Elided stretches are an italic muted line with no speaker. Structured outputs use a definition list with display-face terms.

### Install stages
Five panels on stage blues inside one 28px-rounded group. Each holds numbered steps (display-face markers), command boxes with a translucent tint of the stage ink (8%) and a copy pill, and notes with round bullets in the current colour.

### Question tiles
Rounded tone panels with a display-face summary and a plus/minus drawn in CSS. Opening a tile turns it amber with ink text. Only one opens at a time.

### Focus
A 3px outline offset 3px in the current surface's focus colour (`--focus`), defaulting to ink. Ink surfaces (the switch bar, the footer) set it to amber; each install stage sets it to its own stage ink, so focus always contrasts with the ground it is on.

### Motion
Easings are custom out-curves (ease-out cubic-bezier(0.22, 1, 0.36, 1), expo cubic-bezier(0.16, 1, 0.3, 1)); durations 140ms press, 180ms hover, 240ms UI, about 900ms reveals with a 70ms stagger. Hero lines rise out of masks, the hero pair opens with a shutter wipe and its picture settles from 1.12 scale; on scroll, headings rise from masks and each pair's circles slide into overlap. All of it sits inside `prefers-reduced-motion: no-preference` and behind the `js` class, so content is visible without JavaScript and static under reduced motion. The film in "Start a skill" plays only while in view, never autoplays under reduced motion, and has a visible pause button.

## Do's and Don'ts

### Do:
- **Do** build every new accent from the motif: a circle, a pill, or the two-circle pair with the amber lens.
- **Do** alternate sky and sand fields between sections and plates, and let the panel tone and second circle follow the field.
- **Do** set headings and controls in Libre Franklin 700 and all reading text in Source Serif 4.
- **Do** keep monospace for commands, skill names and flags, the things a reader types or copies.
- **Do** put pictures in greyscale inside the circle with the amber lens in multiply; lift the brightness of dark pictures (`--lift`) rather than letting the lens turn them to a blot.
- **Do** set `--focus` on any new dark surface so the focus outline contrasts with its ground.
- **Do** wrap every animation in `prefers-reduced-motion: no-preference` and keep content visible without JavaScript.
- **Do** credit every picture and clip in the footer and in `site/assets/img/credits.json`, with source and licence.
- **Do** use relative asset URLs only (`assets/...`); the page is served from a subpath on GitHub Pages.
- **Do** show real, shortened sessions and state that they are shortened and that wording will differ.

### Don't:
- **Don't** add eyebrows or kickers (small uppercase labels above headings); headings stand alone.
- **Don't** build icon-plus-heading feature tiles or card grids; facts are plain paragraphs with a bold run-in title.
- **Don't** use icon fonts or glyph icons; indicators are drawn with CSS or the motif's own circles.
- **Don't** invent proof: no testimonials, quotes, ratings, star or download counts, logos or statistics.
- **Don't** add shadows, borders or gradients to separate surfaces; step the tone instead.
- **Don't** set amber text on sky or sand, or use amber for anything other than a filled shape.
- **Don't** introduce a new hue; the old logo indigo stays in the favicon file only.
- **Don't** set plain-language example prompts in monospace.
