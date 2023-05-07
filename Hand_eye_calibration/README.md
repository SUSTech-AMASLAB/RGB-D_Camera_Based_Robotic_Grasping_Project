# Hand-eye Calibration Based on ArUco
Below are the two options to obtain the camera-to-base transformation matrix in this project.

## Option 1 (commonly used)
- [hand-eye calibration](https://github.com/HenryWJL/jaka_grasping/tree/main/handeye_calibration)

## Option 2
If the result of the above method is not so promising, you can try this one. 

#### (1) Clone the following repository to your workspace (remember to catkin_make and source)
- [jaka_grasping](https://github.com/HenryWJL/jaka_grasping/tree/main)

#### (2) Print an ArUco target and place it on the upper position of the robot's base-link

#### (3) Start the aruco_ros node
```bash
roslaunch handeye_calibration aruco_start.launch
```

### (4) Obtain the camera-to-base transformation matrix directly
```bash
rosrun handeye_calibration easy_hand_to_eye_calib.py
```
