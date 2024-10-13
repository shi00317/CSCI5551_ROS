#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import time

def main():
    rospy.init_node("pub_node")
    rospy.logwarn("start running pub_node")

    pub = rospy.Publisher("5551_topic", String, queue_size=10)
    rate = rospy.Rate(10)# 10Hz: publish 10 times under 1 sec

    while not rospy.is_shutdown():
        rospy.loginfo_once("Start publish")

        msg = String()
        msg.data="Hello world"+str(time.time())
        pub.publish(msg)


if __name__=="__main__":
    main()