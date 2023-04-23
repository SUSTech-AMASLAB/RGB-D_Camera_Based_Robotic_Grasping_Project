import sys
import time             
import jkrc

robot = jkrc.RC("192.168.2.26")#VMmodel
print("logining")
#robot = jkrc.RC("192.168.2.229")#real
robot.login()
print("login finish!")
robot.get_robot_status()
robot.power_on()
robot.enable_robot()
print("enable finish!")
time.sleep(5)
ret=robot.get_robot_status()
if ret[0] == 0:
    #print("robot_status : "+len(ret[1]))
    print("    errcode : "+str(ret[1][0]))
    print("    inpos : "+str(ret[1][1]))
    print("    powered_on : "+str(ret[1][2]))
    print("    enabled : "+str(ret[1][3]))
    print("    rapidrate : "+str(ret[1][4]))
    print('    is net connect: '+str(ret[1][len(ret[1])-1]))
    ret_end_pos = ret [1]
else:
    print("!!EORROR!! something wrong happend , errorcode is :",ret[0])

while(1):
    time.sleep(2)
    a = robot.get_joint_position()
    ret=robot.get_robot_status()
    print("is net connect:"+str(ret[0])+"  "+str(ret[1][23]))
