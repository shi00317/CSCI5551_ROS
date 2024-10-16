#!/bin/bash
docker build -t ros_lecture .

xhost +local:docker
# rocker --x11 --devices /dev/dri --name 5551 --network host ros_lecture 

docker run -it \
    --network host \
    -e DISPLAY=$DISPLAY -e TURTLEBOT3_MODEL=burger \
    --device /dev/dri \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --name 5551 ros_lecture

