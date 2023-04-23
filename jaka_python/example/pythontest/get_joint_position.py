# -*- coding: utf-8 -*-
import sys
#sys.path.append('D:\\vs2019ws\PythonCtt\lib')
import time      
import jkrc
PI=3.1415926

robot = jkrc.RC("192.168.2.160")#返回一个机器人对象
ret = robot.login()#登录
ret = robot.get_joint_position()
if ret[0] == 0:
    print("the joint position is :",ret[1])
else:
    print("some things happend,the errcode is: ",ret[0])
robot.logout()  #登出 
