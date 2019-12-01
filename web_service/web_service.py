#!/usr/bin/env python
from PIL import Image
import cherrypy
import rospy
from geometry_msgs.msg import PoseStamped
from launcher import Launcher
import threading

class RobotService:

    def __init__(self):
        self.launcher = Launcher()
    
    @cherrypy.expose
    def index(self):
        return open("/web/home.html", "r")

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

if __name__ == '__main__':
    cherrypy.quickstart(RobotService(), '/',"service.conf")