# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\\vs2019ws\PythonCtt\PythonCtt')
import time      
import jkrc
PI=3.1415926

ABS = 0           # 绝对运动
INCR = 1          # 增量运动
Enable = True 
Disable = False

robot = jkrc.RC("192.168.2.160")#返回一个机器人对象
robot.login()#登录
robot.power_on() #上电
robot.enable_robot()
joint_pos=[PI/3,PI/3,-PI/3,PI/4,PI/4,0]
robot.joint_move(joint_pos,ABS,True,1)
robot.servo_move_enable(Enable)  #进入位置控制模式
print("enable")
time.sleep(0.5)
for i in range(200):
    robot.servo_p(cartesian_pose = [1, 0, 0, 0, 0, 0],move_mode = INCR)
    time.sleep(0.008)
for i in range(200):
    robot.servo_p(cartesian_pose = [-1,0, 0, 0, 0, 0],move_mode = INCR)  
    time.sleep(0.008)
robot.servo_move_enable(Disable)#退出位置控制模式
print("disable")
robot.logout()  #登出 
