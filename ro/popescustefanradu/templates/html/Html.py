import os

from ro.popescustefanradu.templates.Base import Renderable
from ro.popescustefanradu.templates.body.Body import BodyView
from ro.popescustefanradu.templates.head.Head import HeadView

dir_path = '/'.join(os.path.abspath(__file__).split('/')[:-1])

with open(dir_path + '/body.html', 'r') as body_html_file:
    body_html = body_html_file.read()


class HtmlModel(object):
    def __init__(self, head: HeadView, body: BodyView):
        self.head, body = head, body


class HtmlView(Renderable):
    def __init__(self, model: HtmlModel, template_location):
        super(HtmlView, self).__init__(model, template_location)
