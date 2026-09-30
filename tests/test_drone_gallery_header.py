from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class DroneGalleryHeaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "mother-of-drones.html").read_text(encoding="utf-8")
        cls.css = (ROOT / "site.css").read_text(encoding="utf-8")

    def test_hero_credit_uses_approved_copy(self):
        self.assertIn(
            '<p class="credit-line">Painting The Sky With Light</p>',
            self.html,
        )
        self.assertNotIn(
            'Drone Artist<span class="dot">&middot;</span>Creative Technologist',
            self.html,
        )

    def test_drone_design_section_shares_actor_reel_layout(self):
        shared_selector = "#reel-gallery,\n.mother-design-section {"
        self.assertIn(shared_selector, self.css)
        shared_rule = self.css.split(shared_selector, 1)[1].split("}", 1)[0]
        for declaration in (
            "width: 100vw;",
            "grid-template-columns: clamp(420px, 38vw, 560px) minmax(420px, 1fr);",
            "gap: clamp(18px, 2.2vw, 34px);",
            "margin-left: calc(50% - 50vw);",
            "padding-right: clamp(18px, 4vw, 64px);",
            "padding-left: clamp(18px, 3vw, 44px);",
        ):
            self.assertIn(declaration, shared_rule)

        self.assertIn(
            "#photo-reel-gallery,\n  #reel-gallery,\n  .mother-design-section {",
            self.css,
        )

    def test_drone_video_thumbnails_use_the_actor_reel_card_structure(self):
        design_section = self.html.split('id="design-work"', 1)[1].split(
            "</section>", 1
        )[0]
        card_class_values = re.findall(
            r'<a class="([^\"]*\bwork-card\b[^\"]*)"',
            design_section,
        )

        self.assertEqual(len(card_class_values), 7)
        for class_value in card_class_values:
            classes = class_value.split()
            self.assertNotIn("video-tile", classes)
            self.assertNotIn("mother-video-tile", classes)

        self.assertNotIn(".mother-video-tile {", self.css)

    def test_all_seven_youtube_thumbnails_remain(self):
        design_section = self.html.split('id="design-work"', 1)[1].split(
            "</section>", 1
        )[0]
        thumbnail_sources = re.findall(
            r'https://img\.youtube\.com/vi/[^\"]+/hqdefault\.jpg',
            design_section,
        )
        self.assertEqual(len(thumbnail_sources), 7)


if __name__ == "__main__":
    unittest.main()
