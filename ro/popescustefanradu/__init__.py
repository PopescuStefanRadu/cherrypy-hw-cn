import cherrypy


class TestWorld(object):
    @cherrypy.expose()
    def index(self):
        return "hello, world!"

    @cherrypy.expose()
    def generate(self):
        return


if __name__ == '__main__':
    cherrypy.quickstart(TestWorld())
