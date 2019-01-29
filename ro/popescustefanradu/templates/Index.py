from typing import List

from ro.popescustefanradu.templates.Script import Script
from ro.popescustefanradu.templates.body.Body import BodyView, BodyModel
from ro.popescustefanradu.templates.head.Head import HeadView, HeadModel
from ro.popescustefanradu.templates.html.Html import HtmlView, HtmlModel


class ContentViewRenderer(object):
    def render(self, title, content, scripts: List[Script] = None) -> str:
        top_navbar_view = TopNavbarView()
        content_view = ContentView()
        footer_view = FooterView()
        body_model = BodyModel(top_navbar_view, content_view, scripts, footer_view)
        body_view = BodyView()
        head_model = HeadModel(title)
        head_view = HeadView(head_model)
        html_model = HtmlModel(head=head_view, body=body_view)
        html_view = HtmlView(html_model)
        return html_view.render()
