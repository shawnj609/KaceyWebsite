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
            '<p class="credit-line">Film<span class="dot">&middot;</span>'
            'TV<span class="dot">&middot;</span>Stage</p>',
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
