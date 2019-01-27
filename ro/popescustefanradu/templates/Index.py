from typing import List

from ro.popescustefanradu.models.Event import Event
from ro.popescustefanradu.templates.Footer import FooterViewModel
from ro.popescustefanradu.templates.Head import HeadModel, HeadView


class IndexBodyModel(object):
    def __init__(self, events: List[Event]):
        self.events = events


class IndexView(object):
    def __init__(self, body_data: IndexBodyModel):
        self.head_data = HeadModel(title="Evenimente caritabile", metas=[], style_sheets=[])
        self.body_data = body_data
        self.footer_data = FooterViewModel()

    def render(self) -> str:
        head = HeadView(self.head_data)
        return head.render()
