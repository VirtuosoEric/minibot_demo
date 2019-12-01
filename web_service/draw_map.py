import rospy,tf,os
from geometry_msgs.msg import PoseWithCovarianceStamped
from PIL import Image
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt 
import threading

def draw(x,y,map_pic):
    width , height = map_pic.size
    plt.imshow(map_pic,cmap ='gray',origin='lower')
    print x,y
    if x != 0 and y != 0:
        plt.scatter(100*x + width/2,(-100*y + height/2), c = 'y',marker = 'o', s = 500)
        plt.imshow(map_pic,cmap ='gray')
        print "haha"
    plt.savefig("./map/show.jpg")
    plt.clf()
        
            
if __name__ == '__main__':
    os.chdir('/home/ubuntu/catkin_ws/src/minibot_demo/web_service/')
    map_pic = Image.open("./map/nav_demo.pgm") 
    draw(0,0,map_pic)
    rospy.init_node('map', anonymous=True)
    listener = tf.TransformListener()
    while not rospy.is_shutdown():
        try:
            position, quaternion = listener.lookupTransform("/map", "/base_link", rospy.Time(0))
            draw(position[0],position[1],map_pic)
        except Exception as e:
            print e
            draw(0,0,map_pic)