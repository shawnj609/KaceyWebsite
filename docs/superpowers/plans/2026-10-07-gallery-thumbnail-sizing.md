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
- Create: `tests/test_gallery_thumbnail_layout.py`
- Modify: `actor.html:9,108`
- Modify: `mother-of-drones.html:9,63`
- Modify: `fire.html:9,49`
- Modify: `site.css:1612-1620,2195-2203`

**Interfaces:**
- Consumes: Existing `.actor-gallery-section`, `.scroll-gallery-heading`, `.work-grid`, `.work-card`, and `.filmmaker-project-grid` rules.
- Produces: A reusable `.full-width-work-gallery` section class used by `#reel-gallery`, `#design-work`, and `#hekates-gallery`.

- [ ] **Step 1: Write the failing regression test**

Create `tests/test_gallery_thumbnail_layout.py`:

```python
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
TARGET_SECTIONS = {
    "actor.html": "reel-gallery",
    "mother-of-drones.html": "design-work",
    "fire.html": "hekates-gallery",
}
CACHE_KEY = "site.css?v=gallery-cards-20261007"


class GalleryThumbnailLayoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = (ROOT / "site.css").read_text(encoding="utf-8")
        cls.pages = {
            name: (ROOT / name).read_text(encoding="utf-8")
            for name in TARGET_SECTIONS
        }

    def css_rule(self, selector):
        match = re.search(
            rf"{re.escape(selector)}\s*\{{(?P<body>[^}}]+)\}}",
            self.css,
            re.DOTALL,
        )
        self.assertIsNotNone(match, selector)
        return match.group("body")

    def test_target_sections_share_full_width_gallery_class(self):
        for page, section_id in TARGET_SECTIONS.items():
            section = re.search(
                rf'<section class="([^"]+)" id="{section_id}"',
                self.pages[page],
            )
            self.assertIsNotNone(section, page)
            self.assertIn("full-width-work-gallery", section.group(1), page)

    def test_target_pages_request_the_new_stylesheet_version(self):
        for page, html in self.pages.items():
            self.assertIn(CACHE_KEY, html, page)

    def test_full_width_gallery_matches_blood_sisters_geometry(self):
        body = self.css_rule(".full-width-work-gallery")
        self.assertIn("width: 100vw", body)
        self.assertIn("grid-template-columns: minmax(0, 1fr)", body)
        self.assertIn("margin-left: calc(50% - 50vw)", body)
        self.assertEqual(body.count("clamp(18px, 4vw, 64px)"), 2)

        work_grid = self.css_rule(".work-grid")
        reference_grid = self.css_rule(".filmmaker-project-grid")
        for declaration in (
            "grid-template-columns: repeat(3, minmax(0, 1fr))",
            "gap: clamp(12px, 1.6vw, 18px)",
        ):
            self.assertIn(declaration, work_grid)
            self.assertIn(declaration, reference_grid)

    def test_shared_gallery_heading_sits_above_the_grid(self):
        body = self.css_rule(
            ".full-width-work-gallery .scroll-gallery-heading"
        )
        self.assertIn("position: relative", body)
        self.assertIn("top: auto", body)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the new test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_gallery_thumbnail_layout -v
```

Expected: FAIL because the target sections do not yet include `.full-width-work-gallery`, the CSS rule does not exist, and the new cache key is absent.

- [ ] **Step 3: Add the shared layout class and cache key to the target pages**

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

- [ ] **Step 4: Implement the shared full-width grid geometry**

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

- [ ] **Step 5: Run the focused test and full test suite**

Run:

```bash
python3 -m unittest tests.test_gallery_thumbnail_layout -v
python3 -m unittest discover -s tests -v
```

Expected: the focused test passes and the complete suite passes with no failures.

- [ ] **Step 6: Verify the rendered layout**

Serve the repository root locally and inspect `actor.html`, `mother-of-drones.html`, and `fire.html` at 934px desktop width and a narrow mobile width.

At 934px, measure the first card in `#blood-sisters`, `#reel-gallery`, `#design-work`, and `#hekates-gallery`. Expected: every card is approximately 276 by 173 pixels, with no more than one pixel of difference.

At mobile width, confirm each target and Blood Sisters renders one full-width `16 / 10` card per row, with no horizontal overflow. Open one playable card in each target gallery and confirm its existing link or modal behavior still works.

- [ ] **Step 7: Commit the implementation**

```bash
git add actor.html mother-of-drones.html fire.html site.css tests/test_gallery_thumbnail_layout.py
git commit -m "fix: unify gallery thumbnail sizing"
```
