Requirements: Intel RealSense D455 camera, ROS find_object_2d package.

Process (2d):

Download the find_object_2d package.

```bash
sudo apt-get install ros-noetic-find-object-2d
```

Start all the nodes of D455 camera.

```bash
roslaunch realsense2_camera rs_camera.launch
```

If you only need object recognition based on 2D images, just run the following command

```bash
rosrun find_object_2d find_object_2d image:=/camera/color/image_raw
```

If you prefer object recognition based on 3D images, please first revise the launch file as below.

```bash
cd /opt/ros/noetic/share/find_object_2d/launch/ros1
sudo gedit find_object_3d.launch
```
```launch
<launch>
	<!-- Example finding 3D poses of the objects detected -->
	<!-- $roslaunch openni_launch openni.launch depth_registration:=true -->
	
	<arg name="object_prefix" default="object"/>
	<arg name="objects_path"  default=""/>
	<arg name="gui"           default="true"/>
	<arg name="approx_sync"   default="true"/>
	<arg name="pnp"           default="true"/>
	<arg name="tf_example"    default="true"/>
	<arg name="settings_path" default="~/.ros/find_object_2d.ini"/>
	
	<arg name="rgb_topic"         default="/camera/color/image_raw"/>
	<arg name="depth_topic"       default="/camera/depth/image_rect_raw"/>
	<arg name="camera_info_topic" default="camera/depth/camera_info"/>
	
	<node name="find_object_3d" pkg="find_object_2d" type="find_object_2d" output="screen">
		<param name="gui" value="$(arg gui)" type="bool"/>
		<param name="settings_path" value="$(arg settings_path)" type="str"/>
		<param name="subscribe_depth" value="true" type="bool"/>
		<param name="objects_path" value="$(arg objects_path)" type="str"/>
		<param name="object_prefix" value="$(arg object_prefix)" type="str"/>
		<param name="approx_sync" value="$(arg approx_sync)" type="bool"/>
		<param name="pnp" value="$(arg pnp)" type="bool"/>
		
		<remap from="rgb/image_rect_color" to="$(arg rgb_topic)"/>
		<remap from="depth_registered/image_raw" to="$(arg depth_topic)"/>
		<remap from="depth_registered/camera_info" to="$(arg camera_info_topic)"/>
	</node>
	
	<!-- Example of tf synchronisation with the objectsStamped message -->
	<node if="$(arg tf_example)" name="tf_example" pkg="find_object_2d" type="tf_example" output="screen">
		<param name="object_prefix" value="$(arg object_prefix)" type="str"/>
	</node>
</launch>
```
