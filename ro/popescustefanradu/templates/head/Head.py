from typing import List

from ro.popescustefanradu.Run import dir_path
from ro.popescustefanradu.templates.Base import Renderable
from ro.popescustefanradu.templates.Stylesheet import Stylesheet

with open(dir_path + "/templates/head/head.html", 'r') as head_html_file:
    head_html = head_html_file.read()


class HeadModel(object):
    def __init__(self, title: str, metas: List[str], style_sheets: List[Stylesheet] = None,
                 hostname: str = "localhost"):
        self.title = title
        self.metas = ['<meta charset="utf-8">',
                      '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">']
        self.metas.extend(metas)
        self.style_sheets = [Stylesheet('resources/bootstrap.css', hostname)]
        self.style_sheets.extend(style_sheets)


class HeadView(Renderable):
    def __init__(self, model: HeadModel):
        _model = {
            'title': model.title,
            'metas': '\r\n'.join(model.metas),
            'style_sheets': '\r\n'.join(map(lambda ss: ss.render(), model.style_sheets))
        }
        super().__init__(_model, dir_path + '/templates/head/head.html')
