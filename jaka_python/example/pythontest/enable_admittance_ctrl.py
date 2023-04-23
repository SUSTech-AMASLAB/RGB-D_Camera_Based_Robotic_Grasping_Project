# -*- coding: utf-8 -*-
import sys
#sys.path.append('D:\\vs2019ws\PythonCtt\lib')
import time      
import jkrc
PI=3.1415926

robot = jkrc.RC("10.5.5.100")#返回一个机器人对象
ret = robot.login()#登录
ret = robot.power_on()
ret = robot.enable_robot()
robot.set_torsenosr_brand(2)
robot.set_torque_sensor_mode(1)
robot.set_compliant_type(1, 1)
print("inint sensor comple")
print("ready to run")
#设置柔顺控制参数
ret = robot.set_admit_ctrl_config(0, 0, 20, 5, 0, 0)
ret = robot.set_admit_ctrl_config(1, 0, 20, 5, 0, 0)
ret = robot.set_admit_ctrl_config(2, 99, 20, 10, 0, 0)
ret = robot.set_admit_ctrl_config(3, 0, 20, 5, 0, 0)
ret = robot.set_admit_ctrl_config(4, 0, 20, 5, 0, 0)
ret = robot.set_admit_ctrl_config(5, 0, 20, 5, 0, 0)
#设置力控拖拽使能，1打开，0关闭
ret = robot.enable_admittance_ctrl(1)
print("enable_admittance_ctrl open！")
print("input any word to quit:")
a = input()
ret = robot.enable_admittance_ctrl(0)
ret = robot.set_admit_ctrl_config(2, 0, 20, 5, 0, 0)
robot.set_torque_sensor_mode(0)

robot.logout()  #登出 
