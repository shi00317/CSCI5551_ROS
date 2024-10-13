#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import time

def callback(msg):
    rospy.loginfo_once("start subscribe to 5551 topic")
    rospy.loginfo(msg.data)

def main():
    rospy.init_node("sub_node")
    rospy.logwarn("start running sub_node")
    rospy.Subscriber("5551_topic", String,callback)
    rospy.spin()

if __name__=="__main__":
    main()