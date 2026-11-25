import unittest
from pathlib import Path


class PilotOffer(unittest.TestCase):
    def test_manual_attribution_and_professional_contact(self):
        text = Path("index.html").read_text(encoding="utf-8")
        section = text.split('id="contacto"', 1)[1].split("</section>", 1)[0]
        self.assertEqual(text.count("PILOTO-CSV"), 1)
        self.assertIn("informe de discrepancias", section)
        self.assertIn('href="https://www.linkedin.com/in/oscarmorelli/"', section)
        self.assertNotIn("<form", section)
