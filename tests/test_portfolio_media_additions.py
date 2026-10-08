from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PageMarkup(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.sections = []
        self.links = []
        self.images = []
        self.stylesheets = []
        self.visible_text = []
        self.active_section = None
        self.active_link = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "section" and attributes.get("id"):
            self.active_section = attributes["id"]
            self.sections.append(attributes["id"])
        if tag == "a":
            attributes["section"] = self.active_section
            attributes["text"] = ""
            self.links.append(attributes)
            self.active_link = attributes
        if tag == "img":
            self.images.append(attributes)
        if tag == "link" and attributes.get("rel") == "stylesheet":
            self.stylesheets.append(attributes.get("href"))

    def handle_endtag(self, tag):
        if tag == "a":
            self.active_link = None
        if tag == "section":
            self.active_section = None

    def handle_data(self, data):
        text = " ".join(data.split())
        if text:
            self.visible_text.append(text)
            if self.active_link is not None:
                self.active_link["text"] = " ".join(
                    part for part in (self.active_link["text"], text) if part
                )


class PortfolioMediaAdditionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.actor = PageMarkup((ROOT / "actor.html").read_text(encoding="utf-8"))
        cls.mother = PageMarkup((ROOT / "mother-of-drones.html").read_text(encoding="utf-8"))
        cls.fire = PageMarkup((ROOT / "fire.html").read_text(encoding="utf-8"))
        cls.about = PageMarkup((ROOT / "about.html").read_text(encoding="utf-8"))
        cls.css = (ROOT / "site.css").read_text(encoding="utf-8")

    def test_nebula_gallery_exposes_existing_and_five_requested_videos(self):
        expected = {
            "https://youtu.be/t-AxDWIOE6o": "t-AxDWIOE6o",
            "https://youtu.be/PgifPvlLQBw": "PgifPvlLQBw",
            "https://youtu.be/BlTLerRJiIU": "BlTLerRJiIU",
            "https://youtube.com/shorts/RlUERpbnBds?feature=share": "RlUERpbnBds",
            "https://youtu.be/9n_YS0tOaAY": "9n_YS0tOaAY",
            "https://youtu.be/hEbx6V_iATU": "hEbx6V_iATU",
        }
        nebula_links = {
            link.get("href"): link
            for link in self.mother.links
            if link.get("section") == "nebula"
        }
        image_sources = {image.get("src") for image in self.mother.images}

        self.assertEqual(set(nebula_links), set(expected))
        for href, video_id in expected.items():
            self.assertIn("reel-card", nebula_links[href].get("class", "").split())
            self.assertEqual(nebula_links[href].get("target"), "_blank")
            self.assertIn("noopener", nebula_links[href].get("rel", "").split())
            self.assertIn(
                f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
                image_sources,
            )

    def test_voiceover_section_follows_blood_sisters_and_precedes_footer(self):
        self.assertLess(
            self.actor.sections.index("blood-sisters"),
            self.actor.sections.index("voiceover"),
        )
        self.assertLess(
            self.actor.sections.index("voiceover"),
            self.actor.sections.index("end-credits"),
        )

    def test_blood_sisters_episodes_are_ordered_without_episode_three(self):
        episode_titles = [
            link.get("text")
            for link in self.actor.links
            if link.get("section") == "blood-sisters"
        ]
        self.assertEqual(
            episode_titles,
            [f"Season 1, Episode {episode}" for episode in (1, 2, *range(4, 17))],
        )

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

    def test_lone_star_swing_exposes_the_real_trailer(self):
        href = "https://youtu.be/KglUUry5vnM"
        links_by_href = {link.get("href"): link for link in self.actor.links}
        image_sources = {image.get("src") for image in self.actor.images}

        self.assertIn(href, links_by_href)
        self.assertIn("reel-card", links_by_href[href].get("class", "").split())
        self.assertIn(
            "https://img.youtube.com/vi/KglUUry5vnM/hqdefault.jpg",
            image_sources,
        )

    def test_lone_star_swing_includes_trailer_and_full_film(self):
        lone_star_links = [
            (link.get("href"), link.get("text"))
            for link in self.actor.links
            if link.get("section") == "lone-star-swing"
        ]
        self.assertEqual(
            lone_star_links,
            [
                ("https://youtu.be/KglUUry5vnM", "Lone Star Swing Trailer"),
                ("https://youtu.be/xChwymiiiWs", "Lone Star Swing"),
            ],
        )

    def test_filmmaker_projects_use_requested_order(self):
        project_order = [
            section
            for section in self.actor.sections
            if section in {"blood-sisters", "lone-star-swing", "anita"}
        ]
        self.assertEqual(
            project_order,
            ["blood-sisters", "lone-star-swing", "anita"],
        )

    def test_filmmaker_gallery_restores_the_credit_heading(self):
        self.assertIn(
            "Written · Directed · Produced",
            " ".join(self.actor.visible_text),
        )

    def test_filmmaker_thumbnails_match_the_three_column_voiceover_scale(self):
        filmmaker_grid_rule = self.css.split(".filmmaker-project-grid {", 1)[1].split("}", 1)[0]
        reel_grid_rule = self.css.split(".work-grid {", 1)[1].split("}", 1)[0]

        self.assertIn(
            "grid-template-columns: repeat(3, minmax(0, 1fr));",
            filmmaker_grid_rule,
        )
        self.assertIn("grid-auto-rows: auto;", filmmaker_grid_rule)
        self.assertIn(
            "grid-template-columns: repeat(3, minmax(0, 1fr));",
            reel_grid_rule,
        )
        self.assertIn("grid-auto-rows: auto;", reel_grid_rule)
        self.assertIn(
            ".filmmaker-project-grid .work-card {\n  aspect-ratio: 16 / 10;",
            self.css,
        )
        self.assertIn(
            ".work-grid .work-card {\n  aspect-ratio: 16 / 10;",
            self.css,
        )

    def test_hekates_torch_exposes_both_resources(self):
        links_by_href = {link.get("href"): link for link in self.fire.links}
        expected_links = (
            "https://dronefiredance.com/",
            "assets/hekates-torch-sponsorship-deck.pdf",
        )

        for href in expected_links:
            self.assertIn(href, links_by_href)
            self.assertEqual(links_by_href[href].get("target"), "_blank")
            self.assertIn("noopener", links_by_href[href].get("rel", "").split())

        self.assertTrue((ROOT / expected_links[1]).is_file())

    def test_new_sections_have_desktop_and_mobile_layout_rules(self):
        for selector in (
            ".hekate-description",
            ".hekate-resource-links",
            ".voiceover-section",
            ".voiceover-hero",
            ".voiceover-grid",
        ):
            self.assertIn(selector, self.css)

        self.assertIn(
            "grid-template-columns: repeat(3, minmax(0, 1fr));",
            self.css,
        )
        self.assertIn(
            ".voiceover-grid,\n  .mother-nebula-section .about-media-grid {\n    grid-template-columns: 1fr;",
            self.css,
        )

    def test_phone_about_gallery_rows_expand_to_card_height(self):
        self.assertIn(
            ".about-media-grid {\n    grid-auto-rows: auto;",
            self.css,
        )

    def test_affected_pages_request_the_updated_stylesheet(self):
        self.assertIn(
            "site.css?v=reconciled-20261007",
            self.actor.stylesheets,
        )
        self.assertIn(
            "site.css?v=reconciled-20261007",
            self.mother.stylesheets,
        )
        self.assertIn(
            "site.css?v=portfolio-media-20260929",
            self.fire.stylesheets,
        )
        self.assertIn(
            "site.css?v=reconciled-20261007",
            self.about.stylesheets,
        )


if __name__ == "__main__":
    unittest.main()
