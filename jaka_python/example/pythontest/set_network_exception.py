# -*- coding: utf-8 -*-
# import sys
# sys.path.append('D:\\vs2019ws\PythonCtt\PythonCtt')
import time      
import jkrc
PI=3.1415926
#运动模式
ABS = 0
INCR= 1
robot = jkrc.RC("192.168.2.194")#返回机器人对象
robot.login()#登录
robot.power_on() #上电
robot.enable_robot()
ret = robot.set_network_exception_handle(100,2)#设置100ms, 暂停运动。  
print(ret)
print("move1")
num=0
while(1):
    robot.joint_move([1,1,1,1,1,1],ABS,False,0.5)
    robot.joint_move([-1,1,1,1,1,1],ABS,False,0.5)
    num = num +1
    print(num)
    time.sleep(0.5)
robot.logout()
