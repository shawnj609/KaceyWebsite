from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ActingMediaMarkup(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.images = []
        self.section = None
        self.link = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "section" and attributes.get("id"):
            self.section = attributes["id"]
        if tag == "a":
            attributes["section"] = self.section
            attributes["text"] = ""
            self.links.append(attributes)
            self.link = attributes
        if tag == "img":
            attributes["section"] = self.section
            self.images.append(attributes)

    def handle_endtag(self, tag):
        if tag == "a":
            self.link = None
        if tag == "section":
            self.section = None

    def handle_data(self, data):
        text = " ".join(data.split())
        if text and self.link is not None:
            self.link["text"] = " ".join(
                part for part in (self.link["text"], text) if part
            )


class ActingReelsAndAnitaTrailersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = ActingMediaMarkup(
            (ROOT / "actor.html").read_text(encoding="utf-8")
        )

    def test_new_acting_reels_are_first(self):
        reel_links = [
            link for link in self.page.links if link.get("section") == "reel-gallery"
        ]
        self.assertEqual(
            [(link.get("href"), link.get("text")) for link in reel_links[:3]],
            [
                ("https://youtu.be/PerPxqa3BvI", "Acting Reel 1"),
                ("https://youtu.be/2b9JGv_YawQ", "Acting Reel 2"),
                ("https://youtu.be/tfEpUExAU3w", "Project Rant"),
            ],
        )

    def test_anita_trailers_follow_the_hero(self):
        anita_links = [
            link for link in self.page.links if link.get("section") == "anita"
        ]
        self.assertEqual(
            [(link.get("href"), link.get("text")) for link in anita_links],
            [
                ("https://youtu.be/f1HC-8zB9Sg", "Anita Trailer 1"),
                ("https://youtu.be/eE0cpQRpLPE", "Anita Trailer 2"),
            ],
        )

    def test_new_cards_have_accessible_fallbacks_and_thumbnails(self):
        expected = {
            "PerPxqa3BvI": "Acting Reel 1",
            "2b9JGv_YawQ": "Acting Reel 2",
            "f1HC-8zB9Sg": "Anita Trailer 1",
            "eE0cpQRpLPE": "Anita Trailer 2",
        }
        links = {link.get("href"): link for link in self.page.links}
        images = {image.get("src"): image for image in self.page.images}

        for video_id, title in expected.items():
            href = f"https://youtu.be/{video_id}"
            thumbnail = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            self.assertIn(href, links)
            self.assertIn(thumbnail, images)
            link = links[href]
            self.assertEqual(link.get("text"), title)
            self.assertIn("reel-card", link.get("class", "").split())
            self.assertEqual(link.get("target"), "_blank")
            self.assertIn("noopener", link.get("rel", "").split())
            image = images[thumbnail]
            self.assertIn(title, image.get("alt", ""))


if __name__ == "__main__":
    unittest.main()
