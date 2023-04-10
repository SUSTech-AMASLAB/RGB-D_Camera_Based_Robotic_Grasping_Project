# RGB-D Camera Based Robotic Grasping Project

> @Brief：该仓库是AMASLAB 基于RGB-D相机的机器人抓取（RGB-D Camera Based Robotic Grasping Project）项目文档。
>
> @Author：[Li Dong](https://github.com/DoongLi)
>
> @Date：2022-10-13
>
> @Github Link：[https://github.com/SUSTech-AMASLAB/RGB-D_Camera_Based_Robotic_Grasping_Project](https://github.com/SUSTech-AMASLAB/RGB-D_Camera_Based_Robotic_Grasping_Project)
>
> @Project Author：[王俊麟](https://github.com/HenryWJL)、[Li Dong](https://github.com/DoongLi)

## Introduction

**Project**：RGB-D Camera Based Robotic Grasping Project /   基于RGB-D相机的机器人抓取项目

 **Requirements**：

- 1.基于相关硬件，完成相机和机械臂手眼标定，并自主识别和抓取任务。
- 2.在本仓库上，撰写相关学习、调试、方案以及相关问题文档，并将能实现上述功能的可重复 系统框架 整合到仓库中。

**Device**：JAKA MiniCobo机械臂、Intel Realsense D455深度相机、工控机。

## Outline

#### 1.阅读实验室协作项目文档

**Requirements**：掌握项目完成流程和相关要求。

**Reference**：[https://github.com/SUSTech-AMASLAB/AMASLAB_Collaboration_Project_Doc](https://github.com/SUSTech-AMASLAB/AMASLAB_Collaboration_Project_Doc)

#### 2.基础内容学习

 **Requirements**：linux（Ubuntu）、Python、C++、ROS

**Reference**：[https://github.com/SUSTech-AMASLAB/Tutorial_for_Direction_Of_Robotics](https://github.com/SUSTech-AMASLAB/Tutorial_for_Direction_Of_Robotics)

#### 3.相关硬件调试

项目相关硬件如下：

- JAKA MiniCobo机械臂：[https://github.com/SUSTech-AMASLAB/JAKA-MiniCobo](https://github.com/SUSTech-AMASLAB/JAKA-MiniCobo)
- Intel Realsense D455深度相机：[https://github.com/SUSTech-AMASLAB/Intel_Realsense_Device/blob/main/Intel_Realsense_D455.md](https://github.com/SUSTech-AMASLAB/Intel_Realsense_Device/blob/main/Intel_Realsense_D455.md)(python sdk: https://dev.intelrealsense.com/docs/python2?_ga=2.160094900.843708283.1677650776-238679215.1665986034)
- 工控机：https://github.com/SUSTech-AMASLAB/EPIC-KBS9

#### 4.项目参考方案实现

Reference :

- [https://github.com/JAKARobotics/JAKA_ROS_Driver](https://github.com/JAKARobotics/JAKA_ROS_Driver)
- [https://github.com/QiSheng918/jaka_ros](https://github.com/QiSheng918/jaka_ros)
- [https://github.com/RobotControlAndMachineVisionLaboratory/jaka_controller_tcp_ros](https://github.com/RobotControlAndMachineVisionLaboratory/jaka_controller_tcp_ros)
- [a practice of grasping](https://blog.csdn.net/weixin_45661757/article/details/115894731?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167644242316800192280853%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=167644242316800192280853&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-115894731-null-null.142^v73^insert_down4,201^v4^add_ask,239^v1^insert_chatgpt&utm_term=%E6%9C%BA%E6%A2%B0%E8%87%82%E8%A7%86%E8%A7%89%E6%8A%93%E5%8F%96&spm=1018.2226.3001.4187)
- [another practice of grasping](https://blog.csdn.net/m0_37715028/article/details/126519321?ops_request_misc=&request_id=&biz_id=102&utm_term=%E5%88%A9%E7%94%A8realsense%E7%9B%B8%E6%9C%BA%E5%AE%9A%E4%BD%8D%E7%89%A9%E4%BD%93&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-126519321.142^v73^insert_down4,201^v4^add_ask,239^v2^insert_chatgpt&spm=1018.2226.3001.4187)
- [aucro](https://blog.csdn.net/weixin_45363995/article/details/122494189?ops_request_misc=&request_id=&biz_id=102&utm_term=%E5%A6%82%E4%BD%95%E7%A1%AE%E5%AE%9A%E7%89%A9%E4%BD%93%E5%9C%A8realsense%E7%9B%B8%E6%9C%BA%E5%9D%90%E6%A0%87%E7%B3%BB%E4%B8%AD%E7%9A%84%E4%BD%8D%E5%A7%BF&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-122494189.142^v73^insert_down4,201^v4^add_ask,239^v2^insert_chatgpt&spm=1018.2226.3001.4187)
- [camera calibration](https://blog.csdn.net/weixin_45661757/article/details/113256274)
- [hand-eye calibration](https://blog.csdn.net/qq_27865227/article/details/119650312?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167774596016782427469475%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=167774596016782427469475&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-119650312-null-null.142^v73^pc_new_rank,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=jaka&spm=1018.2226.3001.4187)
- [object detection - opencv](https://blog.csdn.net/qq_52095705/article/details/121568221?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168094072916800222814707%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168094072916800222814707&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-121568221-null-null.142^v82^insert_down1,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=opencv%E7%89%A9%E4%BD%93%E8%AF%86%E5%88%AB&spm=1018.2226.3001.4187)
- [object detection - find_object_2d](https://blog.csdn.net/qq_34935373/article/details/103757619?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168094250916800211517935%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=168094250916800211517935&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-9-103757619-null-null.142^v82^insert_down1,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=find_object_2d&spm=1018.2226.3001.4187)
- [pose estimation](https://docs.opencv.org/3.4/d7/d53/tutorial_py_pose.html)
- [tf](http://wiki.ros.org/tf/Tutorials)
- [Moveit](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/move_group_python_interface/move_group_python_interface_tutorial.html)
- [Moveit_commander](http://docs.ros.org/en/jade/api/moveit_commander/html/index.html)
- [Moveit control 1](https://blog.csdn.net/weixin_45839124/article/details/106801986?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167886179416800180685739%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=167886179416800180685739&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-106801986-null-null.142^v73^insert_down4,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=moveit%20python%20%E6%95%99%E7%A8%8B&spm=1018.2226.3001.4187)
- [Moveit control 2](https://blog.csdn.net/zxxxiazai/article/details/108647836?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167886242416800225517650%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=167886242416800225517650&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-108647836-null-null.142^v73^insert_down4,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=moveit%20python%20&spm=1018.2226.3001.4187)
- [Intel pyrealsense2](https://intelrealsense.github.io/librealsense/python_docs/_generated/pyrealsense2.html#module-pyrealsense2)
- [Open3d](http://www.open3d.org/docs/release/)

#### 5.整理相关项目资料

整理项目视频、图片、文档和工程代码 , **同时项目发布者和协同项目完成者制作项目主页** . 

## File Description

- **README.md**：项目发布者创建的项目说明文档，非必要禁止改动。


