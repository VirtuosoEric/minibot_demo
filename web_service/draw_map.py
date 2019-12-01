import rospy,tf
from geometry_msgs.msg import PoseWithCovarianceStamped
from PIL import Image
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt 
import threading

def draw(x,y):
    im = Image.open("/map/nav_demo.pgm")    
    width , height = im.size
    plt.imshow(im,cmap ='gray',origin='lower')
    print x,y
    if x != 0 and y != 0:
        plt.scatter(100*x+96,(-100*y+96), c = 'y',marker = 'o', s = 500)
        plt.imshow(im,cmap ='gray')
        print "haha"
    plt.savefig("./map/show.jpg")
    plt.clf()
        
            
if __name__ == '__main__':
    draw(0,0)
    rospy.init_node('map', anonymous=True)
    listener = tf.TransformListener()
    while not rospy.is_shutdown():
        try:
            position, quaternion = listener.lookupTransform("/map", "/base_link", rospy.Time(0))
            draw(position[0],position[1])
        except Exception as e:
            print e
            draw(0,0)