# -*- coding: utf-8 -*-
import sys
#sys.path.append('D:\\vs2019ws\PythonCtt\lib')
import time      
import jkrc

robot = jkrc.RC("192.168.2.160")#返回一个机器人对象
ret = robot.login()#登录

ret = robot.get_robot_state()
if ret[0] == 0:
    print("the robot state is :",ret[1])
else:
    print("some things happend,the errcode is: ",ret[0])
robot.logout()  #登出 
