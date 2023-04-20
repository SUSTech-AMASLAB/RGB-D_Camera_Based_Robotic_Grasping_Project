主要参考reference中的handeye calibration以及aruco链接

handeye_calib包中需要修改的地方：
~/launch/aruco/aruco_start_realsense_sdk.launch中的markerId和markerSize（分别表示aruco码的id和实际标定板的宽度（单位m））

~/launch/online/online_hand_to_eye_calib.launch中的arm_pose_topic（修改为jaka自带的/robot_driver/tool_point（详情见/jaka_ROS/））

需要添加的：
jaka_ROS（其实只需要jaka_ros_driver）

aruco功能包（见reference）
