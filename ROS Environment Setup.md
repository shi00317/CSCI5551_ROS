This guide provides step-by-step instructions for setting up the ROS1 Noetic environment on Windows, macOS, and Linux systems.

## Table of Contents
- [Setting Up on Linux (Ubuntu)](#Setting-up-on-ubuntu)
- [Setting Up on non-Linux PC](#Setting-up-on-non-linux)

### Setting-up-on-ubuntu
- Ubuntu 20.04
	- ROS1 Noetic is natively supported on Ubuntu 20.04.
	- If you are using same Ubuntu version,  you can directly following the official installation steps: http://wiki.ros.org/noetic/Installation/Ubuntu.
- Other Ubuntu version
	- refer to ROS docker image section or Virtual Machine section. 
##### Docker ROS image 
- Install Docker runtime by following this instruction: https://docs.docker.com/engine/install/
- Pull ROS1 Noetic image: 
```bash
docker pull osrf/ros:noetic-desktop-full
```
- Install rocker to provide X11 interface for the running GUI application in container: https://github.com/osrf/rocker

### Setting-up-on-non-linux
To install ROS1 Noetic, you need to have Ubuntu system environment. There are several way to achieve this on Windows and Macbook. You can choose any one you prefered.

##### WSL(Windows Subsystem for Linux )
- WSL is a feature of Microsoft Windows that allows developers to run a Linux environment without the need for a separate virtual machine or dual booting.
- Follow the instruction: https://learn.microsoft.com/en-us/windows/wsl/install to install Ubuntu 20.04 system. Make sure you are using WSL2 instead of WSL1.
- Once you have Ubuntu 20.04 system,  you can directly following the official installation steps: http://wiki.ros.org/noetic/Installation/Ubuntu.

##### Virtual machine (recommend for apple silicon Macbook)
- VMware Fusion(Macbook) and VMware Workstation (Windows) is free for personal use. Download the softeware in here: https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion. 
- Download the ubuntu 20.04 system image.
	- intel and amd CPU: https://releases.ubuntu.com/focal/ (download the desktop image)
	- ARM CPU: https://cdimage.ubuntu.com/releases/focal/release/ ( download the server image)
- Only for server image: Follow the video to install ubuntu desktop GUI : https://drive.google.com/drive/folders/1_KbMO5OyEsgDzSCnMikap-dN4_b9TIaE?usp=share_link
- Once you have Ubuntu 20.04 system,  you can directly following the official installation steps: http://wiki.ros.org/noetic/Installation/Ubuntu.
##### Dual-Boot 
- Need to create the Ubuntu image in a usb driver.
- There lots of video in the youtube video teach you how to create this. Here is an example: https://www.youtube.com/watch?v=-iSAyiicyQY
- Once you have Ubuntu 20.04 system,  you can directly following the official installation steps: http://wiki.ros.org/noetic/Installation/Ubuntu.

