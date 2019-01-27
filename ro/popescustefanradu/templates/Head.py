import string
from typing import List

with open('templates/head.html', 'r') as head_html_file:
    head_html = head_html_file.read()


class HeadModel(object):
    def __init__(self, title: str, metas: List[str], style_sheets: List[str]):
        self.title = title
        self.metas = ['<meta charset="utf-8">',
                      '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">']
        self.metas.extend(metas)
        self.style_sheets = ['<link rel="stylesheet" href="">']
        self.style_sheets.extend(style_sheets)


class HeadView(object):
    def __init__(self, head_view_model: HeadModel):
        self._m = head_view_model

    def render(self) -> str:
        tmpl = string.Template(head_html)
        return tmpl.substitute({
            'title': self._m.title,
            'metas': '\r\n'.join(self._m.metas),
            'style_sheets': '\r\n'.join(self._m.style_sheets)
        })
