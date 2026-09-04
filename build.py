#!/usr/bin/env python3
"""Build index.html for Flip's, injecting the vectorized hat logo inline."""
import pathlib, re

HERE = pathlib.Path(__file__).parent
logo = (HERE / "assets" / "flips-logo.svg").read_text()
logo = logo.replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg ')

def mark(cls):
    return logo.replace('<svg ', f'<svg class="{cls}" ', 1)

tpl = (HERE / "template.html").read_text()
html = tpl.replace("<!--LOGO_HERO-->", mark("logo logo-hero"))
html = html.replace("<!--LOGO_FOOT-->", mark("logo logo-foot"))
(HERE / "index.html").write_text(html)
print(f"built index.html  {len(html):,} bytes")
