from ro.popescustefanradu.templates.Base import Renderable


# noinspection PyMissingConstructor
class Stylesheet(Renderable):
    def __init__(self, href: str, hostname: str = "localhost"):
        self.href, self.hostname = href, hostname

    def render(self) -> str:
        return '<link rel="stylesheet" href="' + self.hostname + self.href + '">'
