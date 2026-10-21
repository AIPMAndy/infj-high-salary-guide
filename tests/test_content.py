from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TestSite(unittest.TestCase):
    def test_site_required_files(self):
        for name in ('index.html', 'README.md', 'START-HERE.md', 'assets/site.css', 'assets/site.js', 'data/content.js', '.github/workflows/deploy-pages.yml', 'assets/favicon.svg', 'assets/social-preview.svg'):
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file(), name)

    def test_local_links_exist(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        links = re.findall(r'''(?:href|src)=["']([^"']+)["']''', html)
        for link in links:
            if link.startswith(('https:', 'http:', '#', 'mailto:', 'tel:')):
                continue
            self.assertTrue((ROOT / link.split('#')[0]).is_file(), link)

    def test_editorial_content_counts(self):
        js = (ROOT / 'data/content.js').read_text(encoding='utf-8')
        self.assertEqual(len(re.findall(r"\{name:'", js)), 10, 'should have 10 career options')
        self.assertEqual(len(re.findall(r"\{id:'(?:raise|promotion|credit|scope|meeting|interview|salary-expect|counteroffer|refusal|transfer|no-budget|network)'", js)), 12)
        self.assertEqual(len(re.findall(r"\{id:'d\d\d'", js)), 30)
        self.assertIn('type:', js)

    def test_no_cdn_or_salaries_hardcoded(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertNotIn('fonts.googleapis.com', html)
        self.assertNotIn('cdn.jsdelivr', html)
        self.assertIn('https://metaver.vip/services', html)
        self.assertIn('没有哪个 MBTI 类型', html)

if __name__ == '__main__':
    unittest.main()
