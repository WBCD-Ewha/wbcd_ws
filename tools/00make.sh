#!/bin/bash
source ~/.bashrc
workspace=$(pwd)


gnome-terminal -t "R5Pro" -x  bash -c "cd ${workspace}; cd ..; catkin_make; exec bash;"

