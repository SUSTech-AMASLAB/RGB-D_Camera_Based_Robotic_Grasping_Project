# -*- coding: utf-8 -*-  
import sys  
#sys.path.append('D:\\vs2019ws\PythonCtt\lib')  
import time        
import jkrc  
robot = jkrc.RC("192.168.2.160")#返回一个机器人对象  
robot.login()#登录
robot.set_payload(mass=1,centroid=[0.01,0.02,0.03])
ret=robot.get_payload()
if ret[0]==0:
    print("thepayloadis:",ret[1])
else:
    print("somethingshappend,theerrcodeis:",ret[0])
robot.logout()