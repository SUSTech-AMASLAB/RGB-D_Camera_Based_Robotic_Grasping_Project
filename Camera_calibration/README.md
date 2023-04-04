Requirements: Intel RealSense D455 camera, Calibration Target.

Process:

1. Download the ROS camera_calibration package.
```bash
   sudo apt-get install ros-noetic-camera-calibration
```
2. Start all the nodes of D455 camera.
```bash
   roslaunch realsense2_camera rs_camera.launch
```
3. Run the calibration program and you will see the following interface. Remember to revise the values of size (the number of corner points) and square (the real length of each grid of the calibration target (unit: m))
```bash
   rosrun camera_calibration cameracalibrator.py --size 8x5 --square 0.0285 image:=camera/color/image_raw camera:=/camera/color/camera_info --no-service-check
```
<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Camera_calibration/Img/Img1.png" /></p>

4. Move the calibration target with your hands until the 'Calibrate' button turns green. Click it to start calibrating.
<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Camera_calibration/Img/Img2.png" /></p>

5. After a few seconds, the 'Save' and 'Commit' button will also turn green, which means that calibration is finished. Click 'Save' to save the results. You can find the saving path in the terminal.
<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Camera_calibration/Img/Img3.png" /></p>
<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Camera_calibration/Img/Img4.png" /></p>

6. Run the following commands to unzip the results.
```bash
   cd /tmp
   tar -xzvf calibrationdata.tar.gz
```
