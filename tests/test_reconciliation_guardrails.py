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
        self.assertIn(
            "See What's <span class=\"gold-text\">Next</span>",
            self.pages["about.html"],
        )
        self.assertNotIn(
            "Who Is <span class=\"gold-text\">She?</span>",
            self.pages["about.html"],
        )


if __name__ == "__main__":
    unittest.main()
