## Turtblebot Simulation
- Turtbot Model export
```bash
export TURTLEBOT3_MODEL = burger
```
- Turtlebot Gazebo 
```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
- rqt_graph and rostopic
```bash
rqt_graph

rostopic list
rostopic echo
```

- Turtlebot teleop
```bash
 roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
- Rviz setup
```bash
rviz
#change the fix frame to base_scan
```

---
## ROS with OpenCV
- usb_cam launch
```bash
roslaunch usb_cam usb_cam-test.launch
```
- python ros node
```bash
python3 face_detect.py
```
---
## ROS Package and Lunch File
- create pkg
```bash
catkin_create_pkg pub_pkg rospy std_msgs

cd ../
catkin_make
```
- create scripts
```bash
cd src/pub_pkg
mkdir scripts
cd scripts
code .
```
- publisher.py
```python
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
```
- do same thing for sub_pkg and here is file subscriber.py
```python
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
```
- create launch file lecture_ws.launch
```xml
<launch>
    <node pkg = "pub_pkg" type = "publisher.py" name="pub_node" />
    <node pkg = "sub_pkg" type = "subscriber.py" name="sub_node" launch-prefix = "gnome-terminal -e" />

</launch>

```