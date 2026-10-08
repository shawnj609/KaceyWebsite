# Site History Reconciliation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore every approved local-only portfolio update on top of the published September 29 site without regressing the standalone Fire page, elemental navigation, About page, Nebula placement, or production assets.

**Architecture:** Continue from the isolated `codex/reconcile-published-site` branch based on `origin/main`. Lock production structure with characterization tests, reapply the tested drone-gallery commits, extend the gallery to 16 videos, and implement the actor copy changes with focused static HTML regression tests.

**Tech Stack:** Plain HTML5, CSS, Python 3 `unittest`, GitHub Pages static deployment.

## Global Constraints

- Preserve `fire.html` as a standalone page and keep it in `.github/workflows/deploy-pages.yml`.
- Preserve Earth / Air / Fire / See navigation on every public page.
- Keep Nebula on `mother-of-drones.html` and Hekate's Torch on `fire.html`.
- Preserve the published About page headed `See What's Next`.
- Do not add frameworks, package managers, third-party runtime dependencies, or raw staging `.mov` files.
- Work only in the isolated reconciliation worktree; leave the original dirty checkout untouched.
- Do not push to `main` until Kacey approves the localhost preview and explicitly authorizes the push.

---

### Task 1: Lock the Published Page Structure

**Files:**
- Create: `tests/test_reconciliation_guardrails.py`

**Interfaces:**
- Consumes: Published `index.html`, `actor.html`, `mother-of-drones.html`, `fire.html`, `about.html`, and `.github/workflows/deploy-pages.yml`.
- Produces: Static regression checks protecting the standalone Fire page and the approved content placement during later tasks.

- [ ] **Step 1: Add the characterization test**

```python
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PAGES = (
    "index.html",
    "actor.html",
    "mother-of-drones.html",
    "fire.html",
    "about.html",
)


class ReconciliationGuardrailsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {
            name: (ROOT / name).read_text(encoding="utf-8")
            for name in PUBLIC_PAGES
        }
        cls.workflow = (
            ROOT / ".github/workflows/deploy-pages.yml"
        ).read_text(encoding="utf-8")

    def test_fire_page_remains_standalone_and_deployed(self):
        self.assertTrue((ROOT / "fire.html").is_file())
        self.assertIn("cp fire.html _site/", self.workflow)
        for name, html in self.pages.items():
            self.assertIn('href="fire.html"', html, name)

    def test_nebula_remains_on_mother_of_drones(self):
        self.assertIn('id="nebula"', self.pages["mother-of-drones.html"])
        self.assertNotIn('id="nebula"', self.pages["about.html"])

    def test_hekates_torch_remains_on_fire(self):
        self.assertIn("Hekate&rsquo;s", self.pages["fire.html"])
        self.assertNotIn('id="hekates-torch"', self.pages["mother-of-drones.html"])

    def test_published_about_page_is_preserved(self):
        self.assertIn("See What's <span class=\"gold-text\">Next</span>", self.pages["about.html"])
        self.assertNotIn("Who Is <span class=\"gold-text\">She?</span>", self.pages["about.html"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the guardrails against the published baseline**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_reconciliation_guardrails.py -v`

Expected: PASS with 4 tests, proving the production structure is protected before feature edits.

- [ ] **Step 3: Commit the guardrails**

```bash
git add tests/test_reconciliation_guardrails.py
git commit -m "test: protect published site structure"
```

---

### Task 2: Restore and Extend the Drone Gallery

**Files:**
- Modify: `mother-of-drones.html:9,42-110`
- Modify: `site.css:283-289,1618-1625,2200-2207`
- Create via recovered commit, then modify: `tests/test_drone_gallery_header.py`

**Interfaces:**
- Consumes: The published YouTube modal behavior and shared `.work-card`, `.reel-card`, `#reel-gallery`, and responsive layout rules.
- Produces: A 16-card Design Work gallery, the approved hero credit, and regression coverage for exact order and presentation.

- [ ] **Step 1: Reapply the two tested drone implementation commits**

Run:

```bash
git cherry-pick ac77291
git cherry-pick 5bafe0e
```

Expected: Both commits apply cleanly. The page now has `Painting The Sky With Light`, shared actor-reel sizing, and the 13-video playlist while retaining Fire and Nebula.

- [ ] **Step 2: Expand the expected gallery data before changing HTML**

Insert these entries at the beginning of `EXPECTED_DRONE_DESIGN_VIDEOS` in `tests/test_drone_gallery_header.py`:

```python
    ("CrQbV0Hd5n0", "Necker Island Show vs Render"),
    ("J-3Gb_1-C48", "2023 Necker Island New Years Show Render"),
    ("h5r-xJK7PQU", "Chinese New Year Render and Show - Stacked"),
```

- [ ] **Step 3: Run the focused test to verify it fails**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_drone_gallery_header.py -v`

Expected: FAIL in the exact playlist/card comparison because the HTML still contains 13 cards instead of 16.

- [ ] **Step 4: Add the three recovered cards at the start of Design Work**

Insert the following immediately inside `.mother-design-grid`, before the existing `wPpaF_1U5SU` card:

```html
        <a class="work-card reel-card reveal-on-scroll" href="https://youtu.be/CrQbV0Hd5n0" target="_blank" rel="noopener" aria-label="Necker Island Show vs Render">
          <img src="https://img.youtube.com/vi/CrQbV0Hd5n0/hqdefault.jpg" alt="Necker Island Show vs Render"/>
          <span class="play-mark" aria-hidden="true"></span>
          <span>Necker Island Show vs Render</span>
        </a>
        <a class="work-card reel-card reveal-on-scroll" href="https://youtu.be/J-3Gb_1-C48" target="_blank" rel="noopener" aria-label="2023 Necker Island New Years Show Render">
          <img src="https://img.youtube.com/vi/J-3Gb_1-C48/hqdefault.jpg" alt="2023 Necker Island New Years Show Render"/>
          <span class="play-mark" aria-hidden="true"></span>
          <span>2023 Necker Island New Years Show Render</span>
        </a>
        <a class="work-card reel-card reveal-on-scroll" href="https://youtu.be/h5r-xJK7PQU" target="_blank" rel="noopener" aria-label="Chinese New Year Render and Show - Stacked">
          <img src="https://img.youtube.com/vi/h5r-xJK7PQU/hqdefault.jpg" alt="Chinese New Year Render and Show - Stacked"/>
          <span class="play-mark" aria-hidden="true"></span>
          <span>Chinese New Year Render and Show - Stacked</span>
        </a>
```

- [ ] **Step 5: Advance the Mother of Drones stylesheet cache key**

Change its stylesheet URL to:

```html
  <link rel="stylesheet" href="site.css?v=reconciled-20261007"/>
```

Update the affected-page stylesheet assertion in `tests/test_portfolio_media_additions.py` to expect `site.css?v=reconciled-20261007` for Mother of Drones while leaving Fire unchanged.

- [ ] **Step 6: Run drone, guardrail, and portfolio tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests/test_drone_gallery_header.py \
  tests/test_reconciliation_guardrails.py \
  tests/test_portfolio_media_additions.py -v
```

Expected: PASS. The guardrails prove Fire and Nebula were not displaced.

- [ ] **Step 7: Commit the completed drone recovery**

```bash
git add mother-of-drones.html site.css tests/test_drone_gallery_header.py tests/test_portfolio_media_additions.py
git commit -m "feat: restore complete drone design gallery"
```

---

### Task 3: Restore Actor Reel Titles and Voiceover

**Files:**
- Modify: `actor.html:9,42,116-169,303-321`
- Create: `tests/test_actor_reel_titles.py`
- Modify: `tests/test_portfolio_media_additions.py:107-127,234-246`

**Interfaces:**
- Consumes: Existing actor Reel Gallery order and URLs, Voiceover gallery markup, and modal behavior.
- Produces: Exact title-to-URL mapping, `Film · TV · Stage`, four ordered voiceover cards, and regression coverage.

- [ ] **Step 1: Add the failing actor-title test**

```python
from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_REELS = [
    ("https://youtu.be/tfEpUExAU3w", "Project Rant"),
    ("https://youtu.be/PCdNapCFjbc", "Chumps"),
    ("https://youtu.be/wD5IjAJgzrs", "Trojan"),
    ("https://youtu.be/4lVvTg29w3U", "Kleenex"),
    ("https://youtu.be/GNntJ3MHVKo", "Grande"),
    ("https://youtu.be/UM1hGwDo1gk", "Nike"),
    ("https://youtu.be/iubvJKyNLTQ", "What's Your Emergency?"),
    ("https://youtu.be/X5gJFi9Q2M4", "Barton Underwater"),
    ("https://youtu.be/Ib8Ktt7GGVE", "Amazon Underwater"),
    ("https://youtu.be/NWGjttVDpV8", "Undo Part One"),
    ("https://youtu.be/ol8Y2hsiPqg", "Undo Part Two"),
]


class ReelParser(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.section = None
        self.active_link = None
        self.reels = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "section":
            self.section = attributes.get("id")
        if tag == "a" and self.section == "reel-gallery":
            self.active_link = {**attributes, "text": "", "alt": ""}
            self.reels.append(self.active_link)
        if tag == "img" and self.active_link is not None:
            self.active_link["alt"] = attributes.get("alt", "")

    def handle_endtag(self, tag):
        if tag == "a":
            self.active_link = None
        if tag == "section":
            self.section = None

    def handle_data(self, data):
        if self.active_link is not None:
            text = " ".join(data.split())
            if text:
                self.active_link["text"] = text


class ActorReelTitlesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "actor.html").read_text(encoding="utf-8")
        cls.page = ReelParser(cls.html)

    def test_hero_credit_uses_approved_order(self):
        self.assertIn(
            '<p class="credit-line">Film<span class="dot">&middot;</span>TV<span class="dot">&middot;</span>Stage</p>',
            self.html,
        )

    def test_reel_urls_titles_and_alt_text_match(self):
        self.assertEqual(
            [(reel["href"], reel["text"]) for reel in self.page.reels],
            EXPECTED_REELS,
        )
        self.assertEqual(
            [reel["alt"] for reel in self.page.reels],
            [f"{title} acting reel preview" for _url, title in EXPECTED_REELS],
        )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Update the portfolio voiceover test before changing HTML**

Replace `test_voiceover_cards_expose_the_three_requested_demos` with:

```python
    def test_voiceover_cards_use_recovered_order(self):
        expected = [
            ("Fef8IC-1ktg", "Talk Dirty To Me Intro"),
            ("wHCtd7lAQPw", "A Voice in the Wilderness"),
            ("78CZWQVsmXA", "Dell VO Demo"),
            ("1SMoIUaqG6A", "Micro Power VO Demo"),
        ]
        voiceover_links = [
            link
            for link in self.actor.links
            if link.get("section") == "voiceover"
        ]
        image_sources = {image.get("src") for image in self.actor.images}

        self.assertEqual(
            [(link.get("href"), link.get("text")) for link in voiceover_links],
            [(f"https://youtu.be/{video_id}", title) for video_id, title in expected],
        )
        for link, (video_id, _title) in zip(voiceover_links, expected):
            self.assertIn("reel-card", link.get("class", "").split())
            self.assertEqual(link.get("target"), "_blank")
            self.assertIn("noopener", link.get("rel", "").split())
            self.assertIn(
                f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
                image_sources,
            )
```

- [ ] **Step 3: Run the actor tests to verify they fail**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests/test_actor_reel_titles.py \
  tests/test_portfolio_media_additions.py -v
```

Expected: FAIL because the hero credit still begins with TV, reel captions are generic, and Talk Dirty To Me is absent.

- [ ] **Step 4: Replace the actor credit and reel text**

Change the hero credit to:

```html
        <p class="credit-line">Film<span class="dot">&middot;</span>TV<span class="dot">&middot;</span>Stage</p>
```

For the eleven existing reel cards, keep URLs in place and replace captions and image alternative text using `EXPECTED_REELS`, with alternative text formatted as `<title> acting reel preview`.

- [ ] **Step 5: Add Talk Dirty To Me first in Voiceover**

Insert before `A Voice in the Wilderness`:

```html
        <a class="work-card reel-card reveal-on-scroll" href="https://youtu.be/Fef8IC-1ktg" target="_blank" rel="noopener">
          <img src="https://img.youtube.com/vi/Fef8IC-1ktg/hqdefault.jpg" alt="Talk Dirty To Me Intro voiceover demo preview"/>
          <span class="play-mark" aria-hidden="true"></span>
          <span>Talk Dirty To Me Intro</span>
        </a>
```

- [ ] **Step 6: Advance the actor stylesheet cache key**

Change the stylesheet URL to:

```html
  <link rel="stylesheet" href="site.css?v=reconciled-20261007"/>
```

Update the affected-page stylesheet assertion in `tests/test_portfolio_media_additions.py` to expect that value for Actor.

- [ ] **Step 7: Run the actor and full static suites**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests/test_actor_reel_titles.py \
  tests/test_portfolio_media_additions.py -v
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Expected: PASS with no regressions.

- [ ] **Step 8: Commit the actor recovery**

```bash
git add actor.html tests/test_actor_reel_titles.py tests/test_portfolio_media_additions.py
git commit -m "feat: restore actor reel titles and voiceover"
```

---

### Task 4: Verify the Reconciled Site and Prepare Preview

**Files:**
- Verify: `index.html`
- Verify: `actor.html`
- Verify: `mother-of-drones.html`
- Verify: `fire.html`
- Verify: `about.html`
- Verify: `site.css`
- Verify: `.github/workflows/deploy-pages.yml`

**Interfaces:**
- Consumes: The completed static site and regression suite.
- Produces: A clean, locally previewable reconciliation branch ready for Kacey's review.

- [ ] **Step 1: Run repository integrity checks**

Run:

```bash
git diff --check origin/main...HEAD
git status --short
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Expected: No whitespace errors, only intended files changed, and all tests pass.

- [ ] **Step 2: Confirm production links and assets exist**

Run:

```bash
for page in index.html actor.html mother-of-drones.html fire.html about.html; do
  test -f "$page"
  grep -q 'href="fire.html"' "$page"
done
test -f assets/hekates-torch-sponsorship-deck.pdf
grep -q 'cp fire.html _site/' .github/workflows/deploy-pages.yml
```

Expected: Exit code 0.

- [ ] **Step 3: Start the local preview server**

Run: `python3 -m http.server 8081`

Expected: The server remains available at `http://localhost:8081/` from the reconciliation worktree. Use 8081 because the original checkout may already use 8080.

- [ ] **Step 4: Inspect desktop and mobile layouts**

Verify at desktop and mobile widths:

- Home navigation reaches Earth, Air, Fire, and See pages.
- Fire remains standalone and its sponsorship link is present.
- Mother of Drones shows `Painting The Sky With Light`, 16 Design Work cards, and Nebula below.
- Actor shows the eleven approved reel titles, `Film · TV · Stage`, and four voiceover demos.
- Representative actor, drone, Nebula, and Fire video cards open the existing modal.
- No horizontal overflow or broken production image paths are visible.

- [ ] **Step 5: Request localhost approval**

Give Kacey the exact localhost URL. Do not push or merge yet. After approval, ask whether she wants the branch pushed to `main` for publication.
