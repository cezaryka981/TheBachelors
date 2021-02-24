#!/bin/bash

#DATE=$(date +"%Y-%m-%d %H:%M:%S %s")
DATE=$(date +"%Y-%m-%d_%H%M%s")

fswebcam -r 1280x720 --no-banner /home/pi/webcam/$DATE.jpg
