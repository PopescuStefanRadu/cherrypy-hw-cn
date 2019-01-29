from typing import Optional

from ro.popescustefanradu.templates.Base import Renderable


# noinspection PyMissingConstructor
class Script(Renderable):
    def __init__(self, hostname: Optional[str] = None, src: Optional[str] = None, text: Optional[str] = None):
        self.hostname, self.src, self.text = hostname, src, text

        assert ((src or text) is True) and ((src and text) is False)  # only one of them is non-null
        if src:
            assert hostname

    def render(self) -> str:
        if self.src:
            return '<script src="' + self.hostname + self.src + '"></script>'
        if self.text:
            return '<script>' + self.text + '</script>'
