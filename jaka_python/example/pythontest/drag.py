import jkrc
import time

#坐标系
COORD_BASE  = 0
COORD_JOINT = 1
COORD_TOOL  = 2
#运动模式
ABS = 0
INCR= 1

robot = jkrc.RC("192.168.2.160")
robot.login()
robot.power_on()
robot.enable_robot()
robot.drag_mode_enable(True)
ret = robot.is_in_drag_mode()
print(ret)
a = input()
robot.drag_mode_enable(False)
ret = robot.is_in_drag_mode()
print(ret)
robot.logout()
