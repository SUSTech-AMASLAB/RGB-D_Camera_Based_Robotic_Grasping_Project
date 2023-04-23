# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\\vs2019ws\PythonCtt\PythonCtt')
import time      
import jkrc
PI=3.1415926
#坐标系
COORD_BASE  = 0
COORD_JOINT = 1
COORD_TOOL  = 2
#运动模式
ABS = 0
INCR= 1
#关节1~6依次对应0~5,

robot = jkrc.RC("192.168.2.187")#返回机器人对象
robot.login()#登录
robot.power_on() #上电
robot.enable_robot()
print("move1")
robot.jog(0,INCR,COORD_JOINT,30*PI/180,PI/2)
time.sleep(5)#jog为非阻塞指令，运动状态下接收jog指令会被丢弃
print("move2")
robot.jog(0,INCR,COORD_JOINT,5,-PI/2)
time.sleep(0.5)
robot.jog_stop(0)
robot.logout()
