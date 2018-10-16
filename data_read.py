# Function for reading the sensors
#import Estimating_pos_w_IMU
import sensor_reader_class
import time
import math
import numpy as np

def reading_sensors(read_byte):
    if (read_byte[0] == "X") or (read_byte[0] == "Y") or (read_byte[0] =="Z") or (read_byte[0] =="P") or (read_byte[0] =="F"):
        length = len(read_byte)
        if " " not in (read_byte[3:(length-2)]):
            if "-" not in (read_byte[4:(length-2)]):
                vel = float(read_byte[3:(length-2)])
                if read_byte[0] == "X":
                    #print("IMU 1")
                    if read_byte[1] =="1":
                        sensor_reader_class.IMU_time_class.t_A1X.append(time.time())
                        sensor_reader_class.IMU_class.A1X.append(vel)

                    elif read_byte[1] =="2":
                        sensor_reader_class.IMU_time_class.t_A2X.append(time.time())
                        sensor_reader_class.IMU_class.A2X.append(vel)
                        
                    elif read_byte[1] =="3":
                        sensor_reader_class.IMU_time_class.t_A3X.append(time.time())
                        sensor_reader_class.IMU_class.A3X.append(vel)
                        
                elif read_byte[0] == "Y":
                    #print("IMU 2")
                    if read_byte[1] =="1":
                        sensor_reader_class.IMU_time_class.t_A1Y.append(time.time())
                        sensor_reader_class.IMU_class.A1Y.append(vel)
                        
                    elif read_byte[1] =="2":
                        sensor_reader_class.IMU_time_class.t_A2Y.append(time.time())
                        sensor_reader_class.IMU_class.A2Y.append(vel)
                        
                    elif read_byte[1] =="3":
                        sensor_reader_class.IMU_time_class.t_A3Y.append(time.time())
                        sensor_reader_class.IMU_class.A3Y.append(vel)
                        
                elif read_byte[0] == "Z":
                    #print("IMU 3")
                    if read_byte[1] =="1":
                        sensor_reader_class.IMU_time_class.t_A1Z.append(time.time())
                        sensor_reader_class.IMU_class.A1Z.append(vel)
                        
                        
                    elif read_byte[1] =="2":
                        sensor_reader_class.IMU_time_class.t_A2Z.append(time.time())
                        sensor_reader_class.IMU_class.A2Z.append(vel)
                    
                    elif read_byte[1] =="2":
                        sensor_reader_class.IMU_time_class.t_A3Z.append(time.time())
                        sensor_reader_class.IMU_class.A3Z.append(vel)
                        
                        
                elif read_byte[0] == "P":
                    if read_byte[1] == "1":
                        sensor_reader_class.Angle_time_class.t_A1.append(time.time())
                        sensor_reader_class.Angle_class.A1.append(vel)

                    elif read_byte[1] =="2":
                        sensor_reader_class.Angle_time_class.t_A2.append(time.time())
                        sensor_reader_class.Angle_class.A2.append(vel)

                    elif read_byte[1] == "3":
                        sensor_reader_class.Angle_time_class.t_A3.append(time.time())
                        sensor_reader_class.Angle_class.A3.append(vel)

                    elif read_byte[1] =="4":
                        sensor_reader_class.Angle_time_class.t_A4.append(time.time())
                        sensor_reader_class.Angle_class.A4.append(vel)

                    elif read_byte[1] =="5":
                        sensor_reader_class.Angle_time_class.t_A5.append(time.time())
                        sensor_reader_class.Angle_class.A5.append(vel)

                    elif read_byte[1] == "6":
                        sensor_reader_class.Angle_time_class.t_A6.append(time.time())
                        sensor_reader_class.Angle_class.A6.append(vel)

                elif read_byte[0] == "F":
                    if read_byte[1] == "1":
                        sensor_reader_class.Force_time_class.t_F1.append(time.time())
                        sensor_reader_class.Force_class.F1.append(vel)

                    elif read_byte[1] =="2":
                        sensor_reader_class.Force_time_class.t_F2.append(time.time())
                        sensor_reader_class.Force_class.F2.append(vel)

                    elif read_byte[1] == "3":
                        sensor_reader_class.Force_time_class.t_F3.append(time.time())
                        sensor_reader_class.Force_class.F3.append(vel)

                    elif read_byte[1] =="4":
                        sensor_reader_class.Force_time_class.t_F4.append(time.time())
                        sensor_reader_class.Force_class.F4.append(vel)

                    elif read_byte[1] =="5":
                        sensor_reader_class.Force_time_class.t_F5.append(time.time())
                        sensor_reader_class.Force_class.F5.append(vel)

                    elif read_byte[1] == "6":
                        sensor_reader_class.Force_time_class.t_F6.append(time.time())
                        sensor_reader_class.Force_class.F6.append(vel)

                    elif read_byte[1] == "7":
                        sensor_reader_class.Force_time_class.t_F7.append(time.time())
                        sensor_reader_class.Force_class.F7.append(vel)

                    elif read_byte[1] == "8":
                        sensor_reader_class.Force_time_class.t_F8.append(time.time())
                        sensor_reader_class.Force_class.F8.append(vel)

##########################
#### WATCH OUT FOR HOW THINGS ARE MULTIPLIED TOGETHER
##########################

# Homogenious transformation Matrices: Rotation

def rot_ab_x(theta,c_matx,dispx,dispy,dispz):
    c_matx_n = trans_xyz(c_matx, -dispx,-dispy, -dispz)
    c_matx_n = (np.matrix([[1,0.0,0.0,0.],[0.0,math.cos(theta),(-1*math.sin(theta)),0.],[0,math.sin(theta),math.cos(theta), 0.],[0,0,0,1]])*c_matx_n)
    return trans_xyz(c_matx_n, dispx, dispy, dispz)


def rot_ab_y(theta,c_matx, dispx, dispy, dispz):
    c_matx_n = trans_xyz(c_matx, -dispx,-dispy, -dispz)
    c_matx_n =  (np.matrix([[math.cos(theta), 0.0,math.sin(theta),0.0],[0,1,0,0],[(-1*math.sin(theta)),0,math.cos(theta),0],[0,0,0,1]])*c_matx_n)
    return trans_xyz(c_matx_n, dispx, dispy, dispz)

def rot_ab_z_(theta,c_matx,dispx,dispy,dispz):
    c_matx_n = trans_xyz(c_matx, -dispx,-dispy, -dispz)
    c_matx_n = (np.matrix([[math.cos(theta),-math.sin(theta), 0, 0],[math.sin(theta),math.cos(theta), 0, 0],[0,0,1,0],[0,0,0,1]])*c_matx_n)
    return trans_xyz(c_matx_n, dispx, dispy, dispz)


# Homogenious transformation Matrices: Translation

def trans_xyz(c_matx,x,y,z):
    #return np.matmul(np.matlab([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]),c_matx)
    #id = np.identity(4)
    #id[0][-1] = x
    #id[1][-1] = y
    #id[2][-1] = z
    #return id * c_matx
    return (np.matrix([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])*c_matx)
    
       
def trans_xyz_inv(c_matx,x,y,z):
    #return np.matmul(np.matlab([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]),c_matx)
    id = np.identity(4)
    id[0][-1] = x
    id[1][-1] = y
    id[2][-1] = z
    return id * c_matx
    return (np.linalg.inv(np.matrix([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]))*c_matx)       