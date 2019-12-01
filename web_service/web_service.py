#!/usr/bin/env python
from PIL import Image
import cherrypy,time,os,threading
from launcher import Launcher

class RobotService:

    def __init__(self):
        self.launcher = Launcher()
        time.sleep(1)
        self.launcher.start_nav()
    
    @cherrypy.expose
    def index(self):
        return open("./web/home.html", "r")

    @cherrypy.expose
    def start_nav(self):
        self.launcher.start_nav()
        return 'start Navigation'

    @cherrypy.expose
    def approach_heat(self):
        self.launcher.approach_heat()
        return 'approach heat'

    @cherrypy.expose
    def approach_radiation(self):
        self.launcher.approach_radiation()
        return 'approach radiation'

    @cherrypy.expose
    def go_home(self):
        self.launcher.go_home()
        return 'go home'

    @cherrypy.expose
    def stop(self):
        self.launcher.stop()

if __name__ == '__main__':
    os.chdir('/home/ubuntu/catkin_ws/src/minibot_demo/web_service/')
    cherrypy.quickstart(RobotService(), '/',"service.conf")