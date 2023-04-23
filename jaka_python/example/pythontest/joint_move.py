# -*- coding: utf-8 -*-
# import sys
# sys.path.append('D:\\vs2019ws\PythonCtt\PythonCtt')
import time      
import jkrc
PI=3.1415926
#运动模式
ABS = 0
INCR= 1
joint_pos=[PI/2,PI/3,0,PI/4,0,0]
robot = jkrc.RC("192.168.2.160")#返回机器人对象
robot.login()#登录
robot.power_on() #上电
robot.enable_robot()
print("move1")
robot.joint_move(joint_pos,ABS,True,1)
time.sleep(3)
robot.logout()
