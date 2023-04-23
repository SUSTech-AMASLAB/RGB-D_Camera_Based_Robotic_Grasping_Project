from typing import Counter
import jkrc
import time


robot = jkrc.RC("192.168.2.160")
robot.login()
robot.power_on()
robot.enable_robot()
ret = robot.get_collision_level()#获取当前碰撞等级
print(ret)
robot.set_collision_level(1)#设置碰撞等级
ret = robot.get_collision_level()
print(ret)
num = 0
while(1):
    ret = robot.is_in_collision()
    collision_status = ret[1]
    if collision_status == 1:
        time.sleep(5)
        robot.collision_recover() 	#如果发生了碰撞，从碰撞保护模式恢复
        print(" in collision "+ str(num))
    else:
        print("the robot is not in collision "+ str(num))
    time.sleep(1)
    num=num+1

robot.logout()
