# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\\vs2019ws\PythonCtt\PythonCtt')
import time      
import jkrc
PI=3.1415926
#运动模式
ABS = 0
INCR= 1
tcp_pos=[0,0,-30,0,0,0]
robot = jkrc.RC("192.168.2.160")#返回机器人对象
robot.login()#登录
robot.power_on() #上电
robot.enable_robot()
print("move1")
#阻塞 沿z轴负方向 以10mm/s 运动30mm
ret=robot.linear_move(tcp_pos,INCR,True,10)
print(ret[0])
time.sleep(3)
robot.logout()
