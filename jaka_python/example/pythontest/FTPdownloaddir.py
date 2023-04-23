import sys
import jkrc
import time


robot = jkrc.RC("192.168.2.26")#VMmodel
robot.login()
remote = "/lxxpro/"
local= "C:\\Users\\Administrator\\Desktop\\program\\track\\"
#登陆控制器，需要将192.168.2.229替换为自己控制器的IP
robot.init_ftp_client()
result = robot.download_file(local, remote, 2)
print(result)
robot.close_ftp_client()
robot.logout()

