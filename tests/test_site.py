from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.fragments, self.tags = [], [], []
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        href = attrs.get("href") or ""
        if href.startswith("#") and len(href) > 1:
            self.fragments.append(href[1:])

class SiteTests(unittest.TestCase):
    def test_structure(self):
        text = Path("index.html").read_text(encoding="utf-8")
        page = Page()
        page.feed(text)
        self.assertTrue(text.rstrip().endswith("</html>"))
        self.assertIn("main", page.tags)
        self.assertEqual(len(page.ids), len(set(page.ids)))
        self.assertFalse(set(page.fragments) - set(page.ids))
        self.assertNotIn("tuemail@empresa.com", text)
        self.assertNotIn("TU_ID_AQUI", text)
        self.assertNotIn("tu-usuario.github.io", text)
    def test_professional_contact(self):
        text = Path("index.html").read_text(encoding="utf-8")
        self.assertIn('href="https://www.linkedin.com/in/oscarmorelli/"', text)
        self.assertIn("Contactar por LinkedIn", text)
        self.assertNotIn("vía de contacto directo está pendiente", text)
    def test_portfolio_claims(self):
        text = Path("index.html").read_text(encoding="utf-8")
        self.assertNotIn("+240k", text)
        self.assertNotIn("Datos orientativos basados en proyectos reales.", text)

if __name__ == "__main__":
    unittest.main()
