import sys
import jkrc
import time


robot = jkrc.RC("192.168.2.52")#VMmodel
robot.login()
dir= "/program/"
#登陆控制器，需要将192.168.2.229替换为自己控制器的IP
robot.init_ftp_client()
result = robot.get_ftp_dir("/program/", 0)
print(result)
robot.close_ftp_client()
robot.logout()

