# -*- coding: utf-8 -*-
import sys
#sys.path.append('D:\\vs2019ws\PythonCtt\lib')
import time      
import jkrc
PI = 3.1415926

robot = jkrc.RC("10.5.5.100")#返回一个机器人对象
ret = robot.login()#登录
ret = robot.power_on()
ret = robot.enable_robot()
robot.set_torsenosr_brand(2)
robot.set_torque_sensor_mode(1)
robot.set_compliant_type(1, 1)
print("inint sensor comple")
print("ready to run")
ret = robot.get_joint_position()
joint_pos_origin = ret[1]
joint_pos = ret[1]
print(joint_pos)
joint_pos[3] += PI / 4
if (joint_pos[3] > 265 * PI / 180):
	joint_pos[3] -= PI/2
joint_pos[4] += PI / 4
if (joint_pos[4] > 320 * PI / 180):
	joint_pos[4] -= PI/2
joint_pos[5] += PI / 4
if (joint_pos[5] > 265 * PI / 180):
	joint_pos[5] -= PI
print(joint_pos)
ret = robot.start_torq_sensor_payload_identify(joint_pos)
time.sleep(1)
flag = 1
while (1 == flag):
    ret = robot.get_torq_sensor_identify_staus()
    print(ret)
    time.sleep(1)
    flag = ret[1]
print("identy_finish")
ret = robot.get_torq_sensor_payload_identify_result()
print(ret)
ret = robot.set_torq_sensor_payload()
print(ret)
ret = robot.get_torq_sensor_payload_identify_result()
print(ret)
robot.joint_move(joint_pos_origin,0,1,10)
print("back")
robot.logout()  #登出 
