import cherrypy

from ro.popescustefanradu.templates.Index import IndexView, IndexBodyModel


class HomeController(object):

    @cherrypy.expose()
    def index(self):
        index = IndexView(body_data=IndexBodyModel([]))
        return index.render()
