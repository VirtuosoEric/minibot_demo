import subprocess
import os,sys,time
import signal

class Launcher:

    def __init__(self):
        self.working_path = os.getcwd()

    def start_nav(self):
        self.kill_nav()
        time.sleep(1)
        subprocess.Popen(['bash %s/bash_script/start_roslauch.bash' %self.working_path ],shell=True)

    def kill_nav(self):
        subprocess.call(['pkill', '-f', 'HyphaROS_MiniBot_Nav.launch'])

    def approach_heat(self):
        subprocess.Popen(['bash %s/bash_script/pub_goal.bash' %self.working_path,1,2,3,4,5,6],shell=True)

    def approach_radiation(self):
        subprocess.Popen(['bash %s/bash_script/pub_goal.bash' %self.working_path,1,2,3,4,5,6],shell=True)

    def go_home(self):
        subprocess.Popen(['bash %s/bash_script/pub_goal.bash' %self.working_path],shell=True)
