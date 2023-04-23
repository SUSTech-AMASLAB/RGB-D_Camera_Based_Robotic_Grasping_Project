import jkrc
robot = jkrc.RC("192.168.2.160")
robot.login()
ret = robot.get_tcp_position()
print(ret)
rpy = [ret[1][3], ret[1][4], ret[1][5]]#获取rpy
ret = robot.rpy_to_rot_matrix(rpy)#rpy转换成旋转矩阵
print(ret)
rot_matrix = ret[1]#获取旋转矩阵
ret = robot.rot_matrix_to_rpy(rot_matrix)#旋转矩阵转换成rpy
print(ret)
ret = robot.rot_matrix_to_quaternion(rot_matrix)#旋转矩阵转换成四元数
print(ret)
quaternion = ret[1]
ret = robot.quaternion_to_rot_matrix(quaternion)#旋转矩阵转换成四元数
print(ret)
robot.logout()
