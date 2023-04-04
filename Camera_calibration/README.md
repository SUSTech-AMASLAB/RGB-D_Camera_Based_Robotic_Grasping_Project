In this project, Intel RealSense D455 camera is used
Process:

1. In the terminal, run
```bash
   roslaunch realsense2_camera rs_camera.launch
```

rosrun camera_calibration cameracalibrator.py --size 8x5 --square 0.0285 image:=camera/color/image_raw camera:=/camera/color/camera_info --no-service-check
