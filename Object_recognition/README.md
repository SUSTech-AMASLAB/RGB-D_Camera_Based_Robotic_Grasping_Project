Requirements: Intel RealSense D455 camera, ROS find_object_2d package.

Process:

1. Start all the nodes of D455 camera.

```bash
   roslaunch realsense2_camera rs_camera.launch
```

2. Start recognizing objects using find_object_2d.

```bash
   rosrun find_object_2d find_object_2d image:=/camera/color/image_raw
```
