from typing import List, Optional

from ro.popescustefanradu.Run import dir_path
from ro.popescustefanradu.templates.Base import Renderable
from ro.popescustefanradu.templates.Script import Script


class BodyModel:
    def __init__(self, top_navbar: Optional[Renderable] = None,
                 content: Optional[Renderable] = None,
                 scripts: List[Script] = None,
                 footer: Optional[Renderable] = None,
                 hostname: str = 'localhost'
                 ):
        self.top_navbar = top_navbar if top_navbar else ''
        self.content = content if content else ''
        scripts = scripts if scripts else []
        self.scripts = [
            Script(src='/resources/jquery-3.3.1.js', hostname=hostname),
            Script(src='/resources/popper.min.js', hostname=hostname),
            Script(src='/resources/bootstrap.js', hostname=hostname),
        ]
        self.scripts.extend(scripts)
        self.footer = footer if footer else ''


class BodyView(Renderable):
    def __init__(self, body_model: BodyModel, template_location: str = dir_path + '/templates/body/body.html'):
        super(BodyView, self).__init__(body_model, template_location)
