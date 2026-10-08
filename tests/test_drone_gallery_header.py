from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DRONE_DESIGN_VIDEOS = [
    ("CrQbV0Hd5n0", "Necker Island Show vs Render"),
    ("J-3Gb_1-C48", "2023 Necker Island New Years Show Render"),
    ("h5r-xJK7PQU", "Chinese New Year Render and Show - Stacked"),
    ("wPpaF_1U5SU", "Flipside 25 Effigy Render"),
    ("g6U8P0PHcb4", "FreezerBurn 26 Duck Suff III Render"),
    ("Izd_hZuCFCk", "Four Seasons render"),
    ("BOw-psHSoF0", "Viking Ship Funeral Fire Render"),
    ("IFW1qV5zMw8", "2023 Necker Island New Years Drone Show"),
    ("dx6Sr3N3Gzk", "2023 Burning Man Drone Design Collab with Zeplin"),
    ("n6sXgD5Go80", "Banksey Girl With The Red Balloon Drone Render"),
    ("1oMTPBuUZSo", "2025 ABQ Balloon Fiesta Render"),
    ("TfgDetMAd5s", "Drone Design for Chinese New Year and Marina Bay Sands"),
    ("IOym9A9l5Pw", "2023 4th Drone Design at the Sphere"),
    ("vWwH7TSeENI", "Chinese New Year Render"),
    ("dgYVwMrPL1k", "Chinese New Year Render And Show"),
    ("3YX8aV7nboI", "BigAss Render"),
]


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

        self.assertEqual(
            len(card_class_values),
            len(EXPECTED_DRONE_DESIGN_VIDEOS),
        )
        for class_value in card_class_values:
            classes = class_value.split()
            self.assertNotIn("video-tile", classes)
            self.assertNotIn("mother-video-tile", classes)

        self.assertNotIn(".mother-video-tile {", self.css)

    def test_design_gallery_matches_drone_show_design_playlist(self):
        design_section = self.html.split('id="design-work"', 1)[1].split(
            "</section>", 1
        )[0]
        card_pattern = re.compile(
            r'<a class="work-card reel-card reveal-on-scroll" '
            r'href="https://youtu\.be/([^\"]+)" target="_blank" rel="noopener" '
            r'aria-label="([^\"]+)">\s*'
            r'<img src="https://img\.youtube\.com/vi/([^/]+)/hqdefault\.jpg" '
            r'alt="([^\"]+)"/>\s*'
            r'<span class="play-mark" aria-hidden="true"></span>\s*'
            r'<span>([^<]+)</span>\s*</a>'
        )
        actual_cards = card_pattern.findall(design_section)
        expected_cards = [
            (video_id, title, video_id, title, title)
            for video_id, title in EXPECTED_DRONE_DESIGN_VIDEOS
        ]

        self.assertEqual(actual_cards, expected_cards)
        self.assertNotIn("bO8iNFqhOqs", design_section)


if __name__ == "__main__":
    unittest.main()
