#!/usr/bin/env python
#encoding: utf8

import rospy, cv2, math
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class EdgeDetector():
    def __init__(self):
        sub = rospy.Subscriber("/cv_camera/image_raw", Image, self.get_image)
        self.bridge = CvBridge()
        self.img_org = None
        self.canny = rospy.Publisher("img_canny", Image, queue_size=1)
        self.edge = rospy.Publisher("img_edge", Image, queue_size=1)

    def get_image(self, img):
        try:
            self.img_org = self.bridge.imgmsg_to_cv2(img, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)

    def detect_edge(self):
        if self.img_org is None:
            return None
        img_org = self.img_org
        img_gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
        img_canny = cv2.Canny(img_gray, 40, 80)
        self.monitor(self.canny, img_canny)

        circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 20, param1=80, param2=100, minRadius=80, maxRadius=120)
        img_circle = img_org.copy()

        try:
            for i in circles[0,:]:
                cv2.circle(img_circle, (i[0],i[1]), i[2], (0, 255, 0), 2)
        except:
            pass
        
        self.monitor(self.edge, img_circle)

    def monitor(self, pub, img):
        if img.ndim == 2:
            pub.publish(self.bridge.cv2_to_imgmsg(img, "mono8"))
        elif img.ndim == 3:
            pub.publish(self.bridge.cv2_to_imgmsg(img, "bgr8"))
        else:
            pass


if __name__ == '__main__':
    rospy.init_node('edge_detector')
    ed = EdgeDetector()

    rate = rospy.Rate(10)
    rate.sleep()
    while not rospy.is_shutdown():
        ed.detect_edge()
        rate.sleep()

