# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\\vs2019ws\PythonCtt\PythonCtt')
import time      
import jkrc
import _thread
PI=3.1415926

def print_state(name,robot):
    while(1):
        ret = robot.get_program_state() #查询程序运行状态，0 程序终止或无程序运行，1 程序运行中，2 暂停
        print("the robot program state is:",ret[1])
        time.sleep(1)

robot = jkrc.RC("192.168.2.26")#返回一个机器人对象
robot.login()  #登录
ret = robot.program_load("simple")#加载通过APP编写的脚本 program_test需要自己编写
ret = robot.get_loaded_program()  
print("the loaded program is:",ret[1])
robot.program_run()
_thread.start_new_thread( print_state,("p1_state", robot))
time.sleep(10)
robot.program_pause() #暂停
time.sleep(10)
robot.program_resume() #恢复
time.sleep(10)
robot.program_abort()   #停止
time.sleep(3)
robot.logout()            #登出
