---
name: Kacey Samiee
description: Cold-open cinematic portfolio — candlelight type etched into true black
colors:
  page-black: "#000000"
  surface-black: "#080808"
  ink: "#ffffff"
  muted-silver: "#d7d7d7"
  hairline: "#232323"
  candlelight: "#f3e6cf"
  old-gold: "#c7a04d"
  ember: "#4b2415"
  airspace: "#5b7ea9"
  shadow-olive: "#33302a"
  torchlight: "#7a340e"
typography:
  display:
    fontFamily: "Bodoni Moda, Didot, Bodoni 72, Georgia, serif"
    fontSize: "clamp(2.2rem, 6.1vw, 5.4rem)"
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: "0.22em–0.26em"
    textTransform: uppercase
  headline:
    fontFamily: "Bodoni Moda, Didot, Bodoni 72, Georgia, serif"
    fontSize: "clamp(3.2rem, 7.2vw, 7rem)"
    fontWeight: 700
    lineHeight: 0.84
  body:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(0.98rem, 1.25vw, 1.12rem)"
    fontWeight: 450
    lineHeight: 1.62
  label:
    fontFamily: "Fragment Mono, ui-monospace, Menlo, Consolas, monospace"
    fontSize: "clamp(0.75rem, 0.95vw, 0.875rem)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.16em"
rounded:
  none: "0"
  card: "8px"
  full: "50%"
spacing:
  page-gutter: "16px"
  card-gap: "clamp(12px, 1.6vw, 18px)"
  copy-gap: "clamp(24px, 4vw, 38px)"
  section-pad: "clamp(96px, 14vh, 150px)"
components:
  button-play:
    backgroundColor: "#00000038"
    textColor: "{colors.candlelight}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.85em 1.35em"
  button-play-hover:
    backgroundColor: "#f3e6cf1a"
    textColor: "#fff8ea"
  button-ghost:
    textColor: "{colors.candlelight}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.85em 0"
  work-card:
    backgroundColor: "#f3e6cf0f"
    rounded: "{rounded.card}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
  corner-meta:
    textColor: "#f3e6cfbd"
    typography: "{typography.label}"
  title-rule:
    width: "clamp(64px, 7vw, 104px)"
    height: "1px"
    color: "#f3e6cf99"
  play-mark:
    rounded: "{rounded.full}"
    size: "54px"
---

# Design System: Kacey Samiee

## 1. Overview

**Creative North Star: "The Cold Open"**

The system works like the first three minutes of a film before the title card: true black, a face lit by warm light, type that arrives like credits. Every page shows less than it could — fullscreen video and masked portraits carry the art direction, and the design layer is the connective tissue set on top of them: one spread serif title line, hairline components, call-sheet monospace pinned to the corners of the frame. The visitor arrived referred; the system's job is to make them lean in, not to explain.

Color behaves like production design. The global layer knows only black, white, and candlelight; then each page commits to a single world tint painted over black — Ember on the actor page, Airspace blue on Mother of Drones, Torchlight on the fire page, Shadow Olive on about. Depth is atmospheric rather than architectural: gradient scrims, photos feathered into black with mask-image, soft plumes of shadow. Nothing sits "on top of" the page; everything emerges from the dark.

This system explicitly rejects the Squarespace actor template, influencer energy, the event-vendor site, and edgelord goth (see PRODUCT.md's anti-references, restated in section 6). The menace stays elegant: it lives in what is withheld, never in costume.

**Key Characteristics:**
- True-black canvas with per-page world tints; candlelight is the only global warmth
- Film-title typography: the Marquee — one spread line of Bodoni Moda caps, tracked 0.22–0.26em, with a short hairline rule and a mono credit line beneath; stacked lines remain the section-heading voice, one Old Gold line or word per heading
- Monospace as the call sheet: nav, buttons, captions, corner metadata — never prose
- Components etched, not built: hairline borders and light, no solid fills
- Motion is patient: one easing curve, long reveals, a breathing scroll cue

## 2. Colors: The Candlelit Dark

Warm light against true black; everything chromatic belongs either to the candle or to one page's world.

### Primary
- **Candlelight** (#f3e6cf): The light the site is lit by. Buttons, captions, play marks, subpage headings, hairline component borders (at 22–45% alpha), and body copy over imagery (at 72–88% alpha). If a component glows, it glows this color.
- **Old Gold** (#c7a04d): Tarnished metal catching the light. Reserved for exactly one emphasized line or word per heading (`.gold-text`) and for the hover state of scroll cues. Its scarcity is its power.

### Secondary
- **Ember** (#4b2415): The actor page's world — a burnt-sienna radial glow behind masked portraits, deepening to #160905 at the edges.
- **Airspace** (#5b7ea9): Mother of Drones' world — a steel-blue band lifted from the assets/oh-my.png studio backdrop (running #5b7ea9 to #1d3d5f) for the bio section, with rgba(116,149,190) glows over the gallery blacks.
- **Shadow Olive** (#33302a): The about page's world — an unvarnished backstage olive-umber, falling to #070706.
- **Torchlight** (#7a340e): The fire page's world — the flame orange lifted from the Hekate's Torch footage, glowing as rgba(122,52,14) and rgba(196,92,26) over gallery blacks, falling to #030100.

### Neutral
- **Page Black** (#000000): The body background everywhere. Not near-black — black.
- **Surface Black** (#080808): The barely-there surface step; gallery sections use #050505 as their base coat.
- **Ink** (#ffffff): Nav links, home-menu links, and functional text that must read over video.
- **Muted Silver** (#d7d7d7): The hover state of white — links dim toward silver rather than brightening.
- **Hairline** (#232323): Neutral rules and dividers on solid black.

### Named Rules
**The One World Rule.** Each page commits to exactly one world tint over black. Ember, Airspace, Torchlight, and Shadow Olive never appear on the same surface; a new page means choosing (or creating) its world, not mixing existing ones.

**The Candle Rule.** Candlelight is the only warmth the global layer knows, and Old Gold appears on at most one line per heading stack. When everything is gold, nothing is lit.

## 3. Typography

**Display Font:** Bodoni Moda (variable 400–900, optical-size axis live; falls back to Didot / Bodoni 72 / Georgia)
**Body Font:** Archivo (variable 100–900)
**Label/Mono Font:** Fragment Mono (400 only)

**Character:** A hairline didone shouting quietly over footage, a neutral grotesque staying out of the way, and a typewriter voice doing the paperwork. The pairing is film-title card plus call sheet — glamour and production logistics in the same frame.

### Hierarchy
- **Display / Marquee** (700, clamp(2.2rem, 6.1vw, 5.4rem) on home and ~0.7–0.85× of that on subpages, line-height 1.18, UPPERCASE, tracked 0.26em on home / 0.22em on subpages): Page titles set as one spread line — `KACEY SAMIEE`, `ACTRESS & FILMMAKER`, `MOTHER OF DRONES`, `HEKATE'S TORCH`, `WHO IS SHE?`. Centered marquees carry a `padding-left` equal to the tracking so the line sits truly centered; lines wrap into balanced `nowrap` word-spans on small screens. The only letter-spaced serif in the system.
- **Headline** (700, clamp(3.2rem, 7.2vw, 7rem), line-height 0.84): Section headings and sticky gallery headings, usually in Candlelight with one Old Gold line.
- **Body** (450, clamp(0.98rem, 1.25vw, 1.12rem), line-height 1.62): Bios and running prose in Archivo, colored as Candlelight at 72–88% alpha over world tints, capped at ~430–680px measure.
- **Label** (400, clamp(0.75rem, 0.95vw, 0.875rem), letter-spacing 0.12–0.18em, UPPERCASE): Fragment Mono for nav links, buttons, card captions, scroll cues, and the modal close — the call-sheet voice.

### Named Rules
**The Call-Sheet Rule.** Monospace is justified by screenplay and call-sheet convention, not "technical" signaling. It appears on nav, buttons, captions, credits, and metadata — never in body copy, and never as an eyebrow above headings.

**The Marquee Rule.** Page titles (h1) are one spread line of tracked caps, followed by a short hairline rule and a mono credit line — never a stack. One word may carry Old Gold. Section headings (h2) keep the stacked voice: grids of whole `nowrap` lines at line-height 0.82–0.88, one line in Old Gold. The two treatments never trade places.

**The Credit Line Rule.** Under every page title, a Fragment Mono line of dot-separated facts (`ACTRESS · FILMMAKER · DRONE ARTIST`, `NEBULA · FIRE · FLOW`) at 0.22em tracking, Candlelight at 78% alpha, dots dimmed to 55%. Facts only — roles, worlds, section names — never slogans.

## 4. Elevation

This system has no elevation in the UI sense — nothing lifts, nothing floats on hover. Depth is *atmosphere*: gradient scrims layered over footage, portraits feathered into black with `mask-image` gradients, radial world-tint glows behind content, and soft black plumes under cards and modals. Surfaces emerge from the dark rather than stacking above it.

### Shadow Vocabulary
- **Text halo** (`text-shadow: 0 3px 24px rgba(0, 0, 0, 0.82)`): On every heading and copy block that sits over imagery or video; the guarantee of legibility. Ranges to 0 4px 26–28px on subpages.
- **Card plume** (`box-shadow: 0 22px 64px rgba(0, 0, 0, 0.36)`): Under work cards and gallery tiles — ambient, not directional.
- **Modal plume** (`box-shadow: 0 34px 92px rgba(0, 0, 0, 0.72)`): Under the video modal window only.
- **Portrait drop** (`filter: drop-shadow(0 24px 56px rgba(0, 0, 0, 0.58))`): On the about page's reveal portraits.

### Named Rules
**The Scrim Rule.** Type never touches raw pixels. Between letterforms and footage there is always at least one of: a gradient scrim, a mask feathering the image away, or the text halo. Usually two.

## 5. Components

**Etched, not built.** Every component is hairlines and light scratched into the dark — 1px Candlelight borders, transparent or near-transparent fills, monospace labels. Nothing is a solid slab.

### Buttons
- **Shape:** Sharp corners (border-radius 0); mono uppercase label at 0.14em tracking.
- **Play** (`.btn--play`): 1px Candlelight border at 45% alpha, Candlelight text, near-transparent black fill (rgba(0,0,0,0.22)), padding 0.85em 1.35em, and a CSS-border play triangle before the label — the same triangle as the play mark, so button and video tile speak one language.
- **Hover / Focus:** Border resolves to full Candlelight, fill warms to rgba(243,230,207,0.1), text brightens to #fff8ea; 400ms on the house curve.
- **Ghost** (`.btn--ghost`): No box at all — an underline in Candlelight at 40% alpha that resolves to full Candlelight on hover. For the quieter action.

### Cards / Containers
- **Corner Style:** Gently rounded (8px) — the only radius between 0 and a circle in the system.
- **Background:** Candlelight-tinted glass (rgba(243,230,207,0.06)) behind cover images; video tiles use a gradient wash of Old Gold and world tint over a poster frame.
- **Border:** 1px Candlelight at 22% alpha.
- **Shadow Strategy:** Card plume (section 4); a built-in bottom scrim (`::after`, transparent → rgba(0,0,0,0.72)) keeps captions legible.
- **Caption:** Bottom-right, mono uppercase at 0.14em tracking, Candlelight with text halo.
- **Hover:** Image scales to 1.03 and dims to 0.9 opacity over 220ms — a breath, not a bounce.

### Navigation
- **Corner nav:** Every page carries the same four links (`EARTH · AIR · FIRE · SEE`) pinned to the top-right of the first frame — Fragment Mono uppercase at 0.16em tracking, Ink with text halo; hover dims to Muted Silver (never brightens). The current page's link sits at 56% alpha with `aria-current="page"`. Absolute, not fixed: it scrolls away like a title card.
- **Swap links:** Nav items carry a hidden hover label that replaces the default on hover/focus — each link whispers a second name (`EARTH` → `ACTRESS`, `AIR` → `DRONES`, `FIRE` → `DANCER`, `SEE` → `ARTIST`). The fourth link is the verb, not the sea — the invitation to look. Both labels share one grid cell so nothing reflows on swap.
- **Home mark:** On subpages, the fixed drawn-circles mark (two 24px hairline circles) top-left links home. It carries no menu — the corner nav is the menu.

### The Title Frame (signature layout)
The locked home comp, reused on every hero: call-sheet metadata pinned to the corners of the first viewport around the marquee title.
- **Top-right:** the corner nav.
- **Bottom-left:** the location line (`AUSTIN, TX`) — a static mono `<p>`, Candlelight at 74% alpha.
- **Bottom-right:** the scroll cue — a mono anchor (`SCROLL`, `PHOTOS + REELS`, `BIO + DESIGN WORK`) that breathes on the 2.8s loop and turns Old Gold on hover. Only anchors breathe; the location holds still.
- **Center (or left on actor/about):** marquee title, then the title rule — a 1px Candlelight hairline at 60% alpha, clamp(64px, 7vw, 104px) wide — then the credit line. Left-set frames (`.title-frame--left`) align rule and credit to the text edge.
- The rule motif closes each page too: the same hairline sits above the end-credits booking button.

### The Play Mark (signature)
A 54px hairline circle (1px Candlelight at 82% alpha) with a CSS-border triangle, centered over every reel card and echoed inside `.btn--play`. It is the site's one icon.

### The Video Modal
Fixed overlay at rgba(0,0,0,0.82), a 16:9 window at min(1040px, 100%) with the modal plume, and a circled mono "✕" that inverts to Candlelight fill on hover. Opens in 180ms.

### Motion (behavioral, folded here)
One easing curve — `cubic-bezier(0.22, 1, 0.36, 1)` (`--ease-out`) — and a small duration scale: 180ms (overlays), 220ms (image hovers), 400ms (buttons), 700ms (scroll reveals with 80/150/220ms sibling stagger). Reveals translate up 34px and are gated behind a `.js` class so content is visible by default without JavaScript. The scroll cue breathes (opacity 0.54→1, 2.8s loop). All of it collapses to crossfades under `prefers-reduced-motion`.

## 6. Do's and Don'ts

### Do:
- **Do** design on top of the shipped video and portrait work — the footage is the art direction; add type, structure, and components over it (pull real frames with ffmpeg when mocking).
- **Do** keep type legible over footage with the Scrim Rule: scrim + mask + text halo, never raw type on raw pixels.
- **Do** commit each page to one world tint (Ember #4b2415, Airspace #5b7ea9, Torchlight #7a340e, Shadow Olive #33302a) over Page Black #000000.
- **Do** hold the radius scale to exactly three values: 0 (buttons, heroes), 8px (cards, tiles), 50% (play mark, circles).
- **Do** use the house curve `cubic-bezier(0.22, 1, 0.36, 1)` for all motion, keep reveals `.js`-gated, and ship the `prefers-reduced-motion` crossfade for anything that moves.
- **Do** dim on hover (white → Muted Silver #d7d7d7, images → 0.9 opacity); this site gets quieter when touched, not louder.

### Don't:
- **Don't** build the "Squarespace actor template": headshot hero, résumé grid, credits table, "represented by" footer.
- **Don't** let in "influencer energy": Linktree patterns, follower counts, collab-bait copy, platform logo rows.
- **Don't** drift toward the "event-vendor site": packages, quote forms, "trusted by" logo rows, FAQ accordions.
- **Don't** overcook the danger into "edgelord goth": no skulls, blood-red drenches, or distressed grunge type. The menace lives in what is withheld, never in costume.
- **Don't** set body copy or section eyebrows in Fragment Mono — the Call-Sheet Rule. No tiny uppercase tracked labels above headings, ever.
- **Don't** fill components solid or raise their elevation on hover. If a surface reads as a built slab instead of an etched outline, cut the fill.
- **Don't** replace or cover the background videos with stills, and don't gate content visibility on scroll animation without the `.js` class guard.
- **Don't** introduce a fourth typeface, a fourth radius, a second easing curve, or a world tint mix. The system is small on purpose.
