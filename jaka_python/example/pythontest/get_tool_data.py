# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\\vs2019ws\PythonCtt\PythonCtt')
import time      
import jkrc
PI=3.1415926

robot = jkrc.RC("192.168.2.26") #返回一个机器人对象
robot.login()    					 #登录
ret = robot.get_tool_data(1)    #查询工具坐标系数据
if ret[0] == 0:
    print("the tool data is :",ret)
else:
    print("some things happend,the errcode is: ",ret[0])
robot.set_tool_data(1,[0,0,1,0,0,0],'testlx') #设置工具坐标系数据
time.sleep(0.5)
ret = robot.get_tool_data(1)    #查询工具坐标系数据
if ret[0] == 0:
    print("the tool data is :",ret)
else:
    print("some things happend,the errcode is: ",ret[0])
ret = robot.get_tool_id()     #查询工具坐标系id
print("tool_id",ret)
robot.set_tool_id(1)          #设置工具坐标系数据
time.sleep(0.5)  
ret = robot.get_tool_id()     #查询工具坐标系id
print("tool_id",ret)
robot.logout()

