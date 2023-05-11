# Configuration

Before using JAKA MiniCobo, the following configuration must be done.

## 1 Connection

There are two ways of connection, please see [here](https://github.com/SUSTech-AMASLAB/JAKA-MiniCobo/blob/main/Notes/2.%E6%9C%BA%E6%A2%B0%E8%87%82%E4%BB%A3%E7%A0%81%E8%B0%83%E8%AF%95/2.%E6%9C%BA%E6%A2%B0%E8%87%82%E4%BB%A3%E7%A0%81%E8%B0%83%E8%AF%95.md). In this project, it's a better choice to connect the wifi of JAKA's IPC.

<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Configuration/Img/Img1.png" /></p>

## 2 Python API

You can download some references of JAKA's SDK from [here](https://www.jaka.com/jszl.html). You can also view the tutorials of JAKA's python API from [here](https://github.com/HenryWJL/JAKA-MiniCobo/blob/main/SDK/python%E4%BA%8C%E6%AC%A1%E5%BC%80%E5%8F%91.pdf). After downloading the references, find two documents named "libjakaAPI.so" and "jkrc.so" and move them to the package where you store your Python codes. Next, run the following commands (Remember to replace "path" with the path where you store the above two documents).

```bash
sudo ln -s  /path/libjakaAPI.so  /usr/lib
sudo ldconfig
```

## 3 IDE (option)

If you use IDE (Pycharm, Visual Studio Code, etc.) to write Python codes, it's necessary to let the Python interpreter know where the packages are. In this project, interpreter must know where the ROS packages are. Follow the procedures below to configure your IDE.

#### (1) Open the "Settings" interface and find "Python Interpreter". Click "Show all" to show all the possible interpreters.

<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Configuration/Img/Img2.png" /></p>

#### (2) Click the button as shown in the figure to display all the existing paths.

<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Configuration/Img/Img3.png" /></p>

#### (3) Click "+" and add the two paths (The second path refers to your workspace) 

<p align="center"><img src="https://github.com/HenryWJL/RGB-D_Camera_Based_Robotic_Grasping_Project/blob/main/Configuration/Img/Img4.png" /></p>
