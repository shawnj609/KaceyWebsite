# Gallery Thumbnail Sizing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Actor Reels, Design Work, and Hekate's Gallery use the same full-width thumbnail grid and rendered card size as Blood Sisters.

**Architecture:** Add one semantic layout class to the three target sections and define its geometry in `site.css`. The class will reuse the existing `.work-grid` three-column desktop and one-column mobile behavior while matching Blood Sisters' full-width container and horizontal padding. Update the three target pages' stylesheet cache key so Safari requests the new CSS immediately.

**Tech Stack:** Plain HTML, CSS Grid, Python `unittest`, local static HTTP server, in-app browser inspection.

## Global Constraints

- Preserve the site's plain HTML and CSS architecture.
- Blood Sisters is the exact visual and structural reference.
- Desktop uses three equal columns with the shared `16 / 10` aspect ratio and gallery gap.
- Mobile uses one full-width column at the existing gallery breakpoint.
- Existing artwork, titles, links, play controls, colors, animation, and section order remain unchanged.
- At the 934px preview width, target cards must match Blood Sisters within one pixel.
- Do not introduce horizontal overflow.

---

### Task 1: Share the Blood Sisters gallery geometry

**Files:**
- Modify: `actor.html:9,108`
- Modify: `mother-of-drones.html:9,63`
- Modify: `fire.html:9,49`
- Modify: `site.css:1612-1620,2195-2203`

**Interfaces:**
- Consumes: Existing `.actor-gallery-section`, `.scroll-gallery-heading`, `.work-grid`, `.work-card`, and `.filmmaker-project-grid` rules.
- Produces: A reusable `.full-width-work-gallery` section class used by `#reel-gallery`, `#design-work`, and `#hekates-gallery`.

- [ ] **Step 1: Run the rendered regression check and verify it fails**

At a 934px browser width, measure the first card in `#blood-sisters`, `#reel-gallery`, `#design-work`, and `#hekates-gallery` with `getBoundingClientRect()`.

Expected before implementation: Blood Sisters is approximately 276 by 173 pixels while Actor Reels is approximately 133 by 83 pixels and the other target galleries are also materially narrower. This proves the rendered behavior fails the approved requirement before production code changes.

- [ ] **Step 2: Add the shared layout class and cache key to the target pages**

In `actor.html`, change the Actor Reels section and stylesheet link to:

```html
<link rel="stylesheet" href="site.css?v=gallery-cards-20261007"/>
<section class="actor-gallery-section work-section full-width-work-gallery" id="reel-gallery" aria-labelledby="reel-gallery-title">
```

In `mother-of-drones.html`, change the Design Work section and stylesheet link to:

```html
<link rel="stylesheet" href="site.css?v=gallery-cards-20261007"/>
<section class="actor-gallery-section mother-design-section full-width-work-gallery" id="design-work" aria-labelledby="design-work-title">
```

In `fire.html`, change the Hekate's Gallery section and stylesheet link to:

```html
<link rel="stylesheet" href="site.css?v=gallery-cards-20261007"/>
<section class="actor-gallery-section hekate-gallery-section full-width-work-gallery" id="hekates-gallery" aria-labelledby="hekates-gallery-title">
```

- [ ] **Step 3: Implement the shared full-width grid geometry**

Replace the `#reel-gallery, .mother-design-section` layout rule in `site.css` with:

```css
.full-width-work-gallery {
  width: 100vw;
  grid-template-columns: minmax(0, 1fr);
  gap: clamp(48px, 7vw, 84px);
  margin-left: calc(50% - 50vw);
  padding-right: clamp(18px, 4vw, 64px);
  padding-left: clamp(18px, 4vw, 64px);
}

.full-width-work-gallery .scroll-gallery-heading {
  position: relative;
  top: auto;
  width: min(560px, 100%);
}
```

Inside `@media (max-width: 860px)`, remove `#reel-gallery` and `.mother-design-section` from the narrow `#photo-reel-gallery` override so `.full-width-work-gallery` retains Blood Sisters' full-width geometry. Leave `#photo-reel-gallery` behavior unchanged.

- [ ] **Step 4: Run the full automated test suite**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: the complete suite passes with no failures.

- [ ] **Step 5: Verify the rendered layout**

Serve the repository root locally and inspect `actor.html`, `mother-of-drones.html`, and `fire.html` at 934px desktop width and a narrow mobile width.

At 934px, measure the first card in `#blood-sisters`, `#reel-gallery`, `#design-work`, and `#hekates-gallery`. Expected: every card is approximately 276 by 173 pixels, with no more than one pixel of difference.

At mobile width, confirm each target and Blood Sisters renders one full-width `16 / 10` card per row, with no horizontal overflow. Open one playable card in each target gallery and confirm its existing link or modal behavior still works.

- [ ] **Step 6: Commit the implementation**

```bash
git add actor.html mother-of-drones.html fire.html site.css
git commit -m "fix: unify gallery thumbnail sizing"
```
