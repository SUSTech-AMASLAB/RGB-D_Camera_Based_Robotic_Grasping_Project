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
robot.joint_move(joint_pos =[1,1,1,1,1,1] ,move_mode = 0 ,is_block = True ,speed = 10 )
# print("joint")
# robot.set_traj_config([0.1, 0.1, 25, 100]) #设置轨迹复现参数，仅录制过程有效
# time.sleep(0.1)
# ret = robot.get_traj_config()#获取轨迹复现参数
# print("traj_config:")
# print(ret)
# robot.set_traj_sample_mode(True, 'pythonTrack')#开启轨迹复现采集
# time.sleep(0.1)
# robot.joint_move(joint_pos =[-1,1,1,1,1,1] ,move_mode = 0 ,is_block = True ,speed = 30*3.14/180 )#阻塞运动
# robot.joint_move(joint_pos =[1,1,1,1,1,1] ,move_mode = 0 ,is_block = True ,speed = 30*3.14/180 )
# # robot.jog(2,INCR,COORD_BASE,10,-2)
# # robot.jog(2,INCR,COORD_BASE,10,2)
# robot.set_traj_sample_mode(False, 'pythonTrack')#结束轨迹复现采集
# time.sleep(1)
# res = robot.generate_traj_exe_file('pythonTrack')#将采集到的轨迹复现文件转化为可执行脚本
# print(res)
robot.program_load("track/pythonTrack")#加载轨迹程序
time.sleep(0.1)
robot.program_run()

