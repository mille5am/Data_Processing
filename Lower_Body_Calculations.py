import sensor_reader_class as src
import data_read as dr
import numpy as np
import math

# EVERYTHING IN METERS(hip angle, knee angle, ankle angle)
def InverseKinematics(phi1,phi2,phi3,hip_x,hip_y,hip_z):
    # Hips as Datum
    src.points_on_exo.Hips.append(np.matrix( [[hip_x],[hip_y],[hip_z],[1.]]))
     
    #hips and back thing
    P0a = dr.trans_xyz(src.points_on_exo.Hips[-1],(src.link_length.back)/2,0.0,0.0)
    # Hip Joint Left
    P1a=dr.trans_xyz(src.points_on_exo.Hips[-1],(src.link_length.back)/2,0.0,0.0)
    src.points_on_exo.HipLeft.append(P1a)
    
    # Knee Joint Left
    P2a=dr.trans_xyz(src.points_on_exo.Hips[-1],0.,0.,src.link_length.thigh_left)  
    P2b=dr.rot_ab_x(phi1,P2a,hip_x, hip_y, hip_z)
    P2a=dr.trans_xyz(P2b,(src.link_length.back)/2,0.0,0.0)
    src.points_on_exo.LeftKnee.append(P2a)
    
    # Ankle Joint Left  
    P3a=dr.trans_xyz(src.points_on_exo.Hips[-1],0.,0.,src.link_length.calf_left)        
    P3b=dr.rot_ab_x(phi2, P3a, hip_x, hip_y, hip_z) 
    P3a=dr.trans_xyz(P3b,0.,0.,src.link_length.thigh_left)  
    P3a=dr.rot_ab_x(phi1,P3a,P3b[0],P3b[1],P3b[2])
    P3a=dr.trans_xyz(P3a,(src.link_length.back)/2,0.,0.)
    src.points_on_exo.LeftAnkle.append(P3a)

    # Foot  Left
    P4a=dr.trans_xyz(src.points_on_exo.Hips[-1],0.,0.,src.link_length.foot) 
    P4b=dr.rot_ab_x(phi3,P4a, hip_x, hip_y, hip_z) 
    P4a=dr.trans_xyz(P4b,0.,0.,src.link_length.calf_left)
    P4b=dr.rot_ab_x(phi2,P4a,P4b[0], P4b[1], P4b[2])
    P4a=dr.trans_xyz(P4b,0.,0.,src.link_length.thigh_left)
    P4a=dr.rot_ab_x(phi1,P4a,P4b[0],P4b[1],P4b[2])
    P4a=dr.trans_xyz(P4a,(src.link_length.back)/2,0.,0.)
    src.points_on_exo.LeftFoot.append(P4a)

    
    
def IMU_Correction(IMU_Array):
    Point1 = IMU_Array[-2]
    Point2 = IMU_Array[-1]
    dif = abs(Point1 + Point2)
    if dif < (16) and ((Point1 < 0 and Point2 > 0) or (Point1 > 0 and Point2 < 0)): # checking to see if data jumps to -1 times value
        IMU_Array[-1] = Point2*-1

def JointAngleCheck(aX, aY,aZ):
    IMU_Correction(aX)
    IMU_Correction(aY)
    IMU_Correction(aZ)  
    
def JointAngleCorrection(IMU_Array, time_array):
    derv_top = np.diff(IMU_Array[-3:])
    #print(derv_top)
    derv_bottom = np.diff(time_array[-3:])
    #print(derv_bottom)
    derivative1 = derv_top[0] / derv_bottom[0]
    derivative2 = derv_top[1] / derv_bottom[1]

    if derivative1*derivative2 < 0 or derivative1*derivative2 == 0: # the derivative changes directions 
        derivative_new = derivative2 * -1
        dify =  derivative_new * np.diff(time_array[-2:])
        ynew = dify + IMU_Array[-2]
        IMU_Array[-1] = float(ynew)
    

