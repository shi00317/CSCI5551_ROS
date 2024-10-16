FROM osrf/ros:noetic-desktop-full-focal

RUN apt update && apt install x11-apps git nano -y
RUN apt autoremove && apt clean
# RUN  rm -rf /var/lib/apt/lists/*

WORKDIR /root
RUN cd /root && mkdir -p catkin_ws/src

WORKDIR /root/catkin_ws/src
RUN git clone https://github.com/ROBOTIS-GIT/turtlebot3
RUN git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations
RUN git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs
# RUN cd ../catkin_make
WORKDIR /root

CMD ["bash"]