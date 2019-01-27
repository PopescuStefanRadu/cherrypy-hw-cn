import os

import cherrypy

from ro.popescustefanradu.controllers.HomeController import HomeController

dir_path = '/'.join(os.path.abspath(__file__).split('/')[:-1])
os.chdir(dir_path)

conf = {
    '/resources': {'tools.staticdir.on': True,
                   'tools.staticdir.dir': dir_path + '/resources',
                   }
}


def start_server():
    cherrypy.tree.mount(HomeController(), '/', conf)
    cherrypy.engine.start()


if __name__ == '__main__':
    start_server()
