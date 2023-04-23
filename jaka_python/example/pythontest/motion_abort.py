# -*- coding: utf-8 -*-
import sys
#sys.path.append('D:\\vs2019ws\PythonCtt\lib')
import time      
import jkrc
robot = jkrc.RC("192.168.2.160")#返回一个机器人对象
robot.login()#登录
robot.power_on() #上电
robot.enable_robot()
print("move1")
robot.joint_move(joint_pos=[1,0,0,0,0,0],move_mode=1,is_block=False,speed=0.05)#增量运动
print("wait")
time.sleep(2)
robot.motion_abort()
robot.logout()#登出