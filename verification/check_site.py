"""Check generated Hugo HTML/CSS paths without third-party packages.

Run from the repository root after the README build:
    py verification/check_site.py public --base-url https://kimsungwoon5056-beep.github.io/MyProfile/
This checks output files, not browser layout, execution or network requests.
"""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.ids=set(); self.images=[]; self.lang=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='html':self.lang=a.get('lang')
        if tag=='img':self.images.append(a)
        key='href' if tag in ('a','link') else 'src' if tag in ('script','img','source') else None
        if key and key in a:self.refs.append((tag,a[key]))

def audit(root,base):
    root=root.resolve(); site=urlsplit(base); pages={}; issues=[]; count=0
    for path in root.rglob('*.html'):
        page=Page();page.feed(path.read_text(encoding='utf-8'));pages[path]=page
        if page.lang!='ko':issues.append({'file':str(path.relative_to(root)),'issue':'lang is not ko'})
        for img in page.images:
            if 'alt' not in img:issues.append({'file':str(path.relative_to(root)),'issue':'missing image alt'})
    def inspect(source,ref,anchor=False):
        nonlocal count
        if ref.startswith(('data:','mailto:','tel:')):return
        if not ref or ref=='#':
            issues.append({'file':str(source.relative_to(root)),'issue':'empty reference'});return
        url=urlsplit(urljoin(urljoin(base,source.relative_to(root).as_posix()),ref))
        if url.scheme=='file' or url.hostname in ('localhost','127.0.0.1'):
            issues.append({'file':str(source.relative_to(root)),'issue':'local PC reference','url':ref});return
        if url.scheme=='http':issues.append({'file':str(source.relative_to(root)),'issue':'HTTP reference','url':ref})
        if url.netloc!=site.netloc:return
        count+=1
        if not url.path.startswith(site.path):
            issues.append({'file':str(source.relative_to(root)),'issue':'outside site base path','url':ref});return
        target=root/unquote(url.path[len(site.path):])
        if target.is_dir():target=target/'index.html'
        if not target.is_file():
            issues.append({'file':str(source.relative_to(root)),'issue':'missing file','url':ref});return
        if anchor and url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            issues.append({'file':str(source.relative_to(root)),'issue':'missing anchor','url':ref})
    for path,page in pages.items():
        for tag,ref in page.refs:inspect(path,ref,tag=='a')
    css_count=0
    for path in root.rglob('*.css'):
        for m in re.finditer(r'url\(\s*([\'"]?)(.*?)\1\s*\)',path.read_text(encoding='utf-8')):
            inspect(path,m[2]);css_count+=1
    return {'html_files':len(pages),'css_url_references':css_count,'internal_references':count,'issues':issues}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('output_dir',type=Path);p.add_argument('--base-url',required=True)
    args=p.parse_args()
    if not (args.output_dir/'index.html').is_file():p.error('output_dir must contain index.html')
    result=audit(args.output_dir,args.base_url);print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(result['issues']))
