import sys
import jkrc
import time

robot = jkrc.RC("192.168.2.22")
ret=robot.login()
print(ret)
ret = robot.get_robot_status()
if ret[0] == 0:
    print(len(ret[1]))
    for i in range(len(ret[1])):
        print(str(i)+":"+str(ret[1][i]))
else:
    print("some things happend,the errcode is: ",ret[0])
robot.logout()

