Requirements: Intel RealSense D455 camera, a calibration target.

Process:

1. Download the ROS camera_calibration package.
```bash
   sudo apt-get install ros-noetic-camera-calibration
```

2. Start all the nodes of D455 camera.:
```bash
   roslaunch realsense2_camera rs_camera.launch
```

2. Run the calibration program. Remember to revise the size (the number of corner points) and the square (the real length of each grid of the calibration target (unit: m)):
```bash
   rosrun camera_calibration cameracalibrator.py --size 8x5 --square 0.0285 image:=camera/color/image_raw camera:=/camera/color/camera_info --no-service-check
```
