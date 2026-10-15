"""Regression cases for the checks that gate publication; standard library only."""
import tempfile
import unittest
from pathlib import Path
from check_site import audit

BASE = 'https://example.github.io/MyProfile/'

class SiteChecks(unittest.TestCase):
    def check_html(self, html, files=None):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'index.html').write_text(html,encoding='utf-8')
            for name,content in (files or {}).items():
                path=root/name;path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(content,encoding='utf-8')
            return audit(root,BASE)

    def test_valid_project_paths_korean_anchor_and_css(self):
        result=self.check_html('<html lang="ko"><link href="/MyProfile/style.css"><a href="about/#소개">소개</a><img src="a.svg" alt="장식"></html>',{
            'style.css':'body{background:url(a.svg)}','a.svg':'<svg/>',
            'about/index.html':'<html lang="ko"><h1 id="소개">소개</h1></html>'})
        self.assertEqual(result['issues'],[])
        self.assertEqual(result['css_url_references'],1)

    def test_missing_resource_is_rejected(self):
        self.assertIn('missing file',[x['issue'] for x in self.check_html('<html lang="ko"><img src="missing.png" alt="사진"></html>')['issues']])

    def test_missing_anchor_is_rejected(self):
        self.assertIn('missing anchor',[x['issue'] for x in self.check_html('<html lang="ko"><a href="#missing">이동</a></html>')['issues']])

    def test_domain_root_path_is_rejected(self):
        self.assertIn('outside site base path',[x['issue'] for x in self.check_html('<html lang="ko"><script src="/app.js"></script></html>')['issues']])

    def test_local_and_http_references_are_rejected(self):
        kinds=[x['issue'] for x in self.check_html('<html lang="ko"><a href="http://localhost:1313/">개발</a><script src="http://example.org/a.js"></script></html>')['issues']]
        self.assertIn('local PC reference',kinds);self.assertIn('HTTP reference',kinds)

    def test_empty_link_language_and_alt_are_rejected(self):
        kinds=[x['issue'] for x in self.check_html('<html lang="en"><a href="#">빈 링크</a><img src="a.svg"></html>',{'a.svg':'<svg/>'})['issues']]
        for issue in ['lang is not ko','empty reference','missing image alt']:self.assertIn(issue,kinds)

if __name__=='__main__':unittest.main()
