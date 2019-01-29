import string
from typing import Optional, Any


# noinspection SpellCheckingInspection
class Renderable(object):
    def __init__(self, model: Any, template_location: Optional[str] = None, template: Optional[str] = None):
        self.model = model
        if template_location is not None:
            self.template = open(template_location).read()
        else:
            if template is not None:
                self.template = template
            else:
                raise ValueError('template_location and template cannot be both null')

    def render(self) -> str:
        # TODO rewrite templating engine to handle _model fields .render() when they are renderable, possibly replace
        #  with map
        return string.Template(self.template).substitute(self.model.__dict__)
