import subprocess
import os,sys,time
import signal

class Launcher:

    def __init__(self):
        self.working_path = os.getcwd()

    def start_nav(self):
        self.stop_draw_map()
        self.kill_nav()
        time.sleep(1)
        subprocess.Popen(['bash %s/bash_script/start_nav.bash' %self.working_path ],shell=True)
        self.start_draw_map()

    def kill_nav(self):
        subprocess.call(['pkill', '-f', 'HyphaROS_MiniBot_Nav.launch'])

    def start_draw_map(self):
        subprocess.Popen(['bash %s/bash_script/draw_map.bash' %self.working_path ],shell=True)

    def stop_draw_map(self):
        subprocess.call(['pkill', '-f', 'draw_map.py'])

    def approach_heat(self):
        subprocess.Popen(['bash %s/bash_script/pub_goal.bash 1 2 3 4 5 6' %self.working_path],shell=True)

    def approach_radiation(self):
        subprocess.Popen(['bash %s/bash_script/pub_goal.bash 2 3 4 5 1 7' %self.working_path],shell=True)

    def go_home(self):
        subprocess.Popen(['bash %s/bash_script/pub_goal.bash' %self.working_path],shell=True)

    def stop(self):
        self.kill_nav()
        self.stop_draw_map()

