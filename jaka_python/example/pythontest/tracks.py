import jkrc
import time
import _thread
#坐标系
COORD_BASE  = 0
COORD_JOINT = 1
COORD_TOOL  = 2
#运动模式
ABS = 0
INCR= 1

if __name__ == '__main__':
    robot = jkrc.RC("192.168.2.194")
    robot.login()
    robot.power_on()
    robot.enable_robot()

    robot.joint_move(joint_pos =[1,0.8,1.2,1,1,1] ,move_mode = 0 ,is_block = True ,speed = 10 )
    print("jpoint")
    robot.set_traj_config([0.1, 0.1, 5, 100])
    robot.set_traj_sample_mode(True, 'pythonTrack1')
    time.sleep(1)
    robot.jog(2 , 1 ,0, 10, 20)
    robot.jog(2 , 1 ,0, 10, 20)
    time.sleep(3)
    print("1")
    robot.jog(2 , 1 ,0, 10, -40 )
    time.sleep(6)
    robot.jog(2 , 1 ,0, 10, 20)
    time.sleep(3)
    robot.jog_stop(2)
    robot.set_traj_sample_mode(False, 'pythonTrack1')
    res = robot.generate_traj_exe_file('pythonTrack1')
    print(res)
    time.sleep(0.1)
    res = robot.program_load("track/pythonTrack1")
    print(res)
    time.sleep(0.1)
    num = 1
    # while 1:
    #     print("times:"+ str(num))
    #     num = num+1
    #     robot.program_run()
    #     while(1):
    #         ret = robot.get_program_state() #查询程序运行状态，0 程序终止或无程序运行，1 程序运行中，2 暂停
    #         print("the robot program state is:",ret[1])
    #         time.sleep(2)
    #         if ret[1]==0:
    #             break
    robot.program_run()
    robot.logout()

