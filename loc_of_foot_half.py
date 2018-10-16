import sensor_reader_class as src
import data_read as dr
import numpy as np
import math as mt

# EVERYTHING IN METERS
def loc_of_foot(phi1,phi2,phi3): #,theta4,theta5,phi6,phi7,phi8):
    # Grounded foot
    src.points_on_exo.LeftFoot.append(np.matrix( [[0.],[0.],[0.],[1.]]))

    # Ankle Point Left
    P1a=dr.trans_xyz(src.points_on_exo.LeftFoot[-1],1.,0.0,0.0)
    src.points_on_exo.LeftAnkle.append(P1a)
    
    # Knee Point Left
    P2a=dr.trans_xyz(src.points_on_exo.LeftFoot[-1],0.,0.,src.link_length.calf_left)  
    P2a=dr.rot_ab_x(phi1,P2a,0.,0.,0.)
    P2b=dr.trans_xyz(P2a,1.,0.,0.)
    src.points_on_exo.LeftKnee.append(P2b)
    
    # Hip Point Left  
    P3a=dr.trans_xyz(src.points_on_exo.LeftFoot[-1],0.,0.,src.link_length.thigh_left)        
    P3a=dr.rot_ab_x(phi2,P3a,0.,0.,0.) 
    P3a=dr.trans_xyz(P3a,0.,0.,src.link_length.calf_left)  
    P3a=dr.rot_ab_x(phi1,P3a,0.,0.,0.)
    P3b=dr.trans_xyz(P3a,1.,0.,0.)
    src.points_on_exo.HipLeft.append(P3b)

    # Back Left
    P4a=dr.trans_xyz(src.points_on_exo.LeftFoot[-1],0.,0.,src.link_length.hip_left)
    P4a=dr.rot_ab_x(phi3,P4a,0.,0.,0.) 
    P4a=dr.trans_xyz(P4a,0.,0.,src.link_length.thigh_left)
    P4a=dr.rot_ab_x(phi2,P4a,0.,0.,0.)
    P4a=dr.trans_xyz(P4a,0.,0.,src.link_length.calf_left)
    P4a=dr.rot_ab_x(phi1,P4a,0.,0.,0.)
    P4b=dr.trans_xyz(P4a,1.,0.,0.)
    src.points_on_exo.Hips.append(P4b)

##    # Back Right
##    P5a=dr.trans_xyz(src.points_on_exo.P0[-1],0.,src.link_length.back,0.)
##    P5a=dr.rot_ab_x_disp(theta4,P5a,0.,0.,0.)
##    P5a=dr.trans_xyz(P5a,0.,0.,src.link_length.hip_left)
##    P5a=dr.rot_ab_y_disp(phi3,P5a,0.,0.,0.) 
##    P5a=dr.trans_xyz(P5a,0.,0.,src.link_length.thigh_left)
##    P5a=dr.rot_ab_y_disp(phi2,P5a,0.,0.,0.)
##    P5a=dr.trans_xyz(P5a,0.,0.,src.link_length.calf_left)
##    P5a=dr.rot_ab_y_disp(phi1,P5a,0.,0.,0.)
##    P5b=dr.trans_xyz(P5a,1.,0.,0.)
##    src.points_on_exo.P5.append(P5b)
##
##    # Hip Point Right
##    P6a=dr.trans_xyz(src.points_on_exo.P0[-1],0.0,0.0,-src.link_length.hip_right)  #troublesome
##    P6a=dr.rot_ab_x_disp(theta5,P6a,0.,0.,0.)
##    P6a=dr.trans_xyz(P6a,0.,src.link_length.back,0.)
##    P6a=dr.rot_ab_x_disp(theta4,P6a,0.,0.,0.)
##    P6a=dr.trans_xyz(P6a,0.,0.,src.link_length.hip_left)
##    P6a=dr.rot_ab_y_disp(phi3,P6a,0.,0.,0.) 
##    P6a=dr.trans_xyz(P6a,0.,0.,src.link_length.thigh_left)
##    P6a=dr.rot_ab_y_disp(phi2,P6a,0.,0.,0.)
##    P6a=dr.trans_xyz(P6a,0.,0.,src.link_length.calf_left)
##    P6a=dr.rot_ab_y_disp(phi1,P6a,0.,0.,0.)
##    P6b=dr.trans_xyz(P6a,1.,0.,0.)
##    src.points_on_exo.P6.append(P6b)
##    
##    # Knee Point Right
##    P7a=dr.trans_xyz(src.points_on_exo.P0[-1],0.,0.,-src.link_length.thigh_right)   
##    P7a=dr.rot_ab_y_disp(-phi6,P7a,0.0,0.0,0.)
##    P7a=dr.trans_xyz(P7a,0.,0.,-src.link_length.hip_right)    
##    P7a=dr.rot_ab_x_disp(theta5,P7a,0.0,0.0,0.)  #troublesome
##    P7a=dr.trans_xyz(P7a,0.,src.link_length.back,0.)
##    P7a=dr.rot_ab_x_disp(theta4,P7a,0.,0.,0.)
##    P7a=dr.trans_xyz(P7a,0.,0.,src.link_length.hip_left)
##    P7a=dr.rot_ab_y_disp(phi3,P7a,0.,0.,0.) 
##    P7a=dr.trans_xyz(P7a,0.,0.,src.link_length.thigh_left)
##    P7a=dr.rot_ab_y_disp(phi2,P7a,0.,0.,0.)
##    P7a=dr.trans_xyz(P7a,0.,0.,src.link_length.calf_left)
##    P7a=dr.rot_ab_y_disp(phi1,P7a,0.,0.,0.)
##    P7b=dr.trans_xyz(P7a,1.,0.,0.)
##    src.points_on_exo.P7.append(P7b)
##
##    # Ankle Point Right
##    P8a=dr.trans_xyz(src.points_on_exo.P0[-1],0.0,0.0,-src.link_length.calf_right)
##    P8a=dr.rot_ab_y_disp(-phi7,P8a,0.0,0.0,0.)
##    P8a=dr.trans_xyz(P8a,0.0,0.0,-src.link_length.thigh_right)
##    P8a=dr.rot_ab_y_disp(-phi6,P8a,0.0,0.0,0.)
##    P8a=dr.trans_xyz(P8a,0.0,0.0,-src.link_length.hip_right)  #troublesome
##    P8a=dr.rot_ab_x_disp(theta5,P8a,0.0,0.0,0.)
##    P8a=dr.trans_xyz(P8a,0.,src.link_length.back,0.)
##    P8a=dr.rot_ab_x_disp(theta4,P8a,0.,0.,0.)
##    P8a=dr.trans_xyz(P8a,0.,0.,src.link_length.hip_left)
##    P8a=dr.rot_ab_y_disp(phi3,P8a,0.,0.,0.) 
##    P8a=dr.trans_xyz(P8a,0.,0.,src.link_length.thigh_left)
##    P8a=dr.rot_ab_y_disp(phi2,P8a,0.,0.,0.)
##    P8a=dr.trans_xyz(P8a,0.,0.,src.link_length.calf_left)
##    P8a=dr.rot_ab_y_disp(phi1,P8a,0.,0.,0.)
##    P8b=dr.trans_xyz(P8a,1.,0.,0.)
##    src.points_on_exo.P8.append(P8b)
##
##
##    # Point on foot
##    P9a=dr.trans_xyz(src.points_on_exo.P0[-1],-1,0.,0.)
##    P9a=dr.rot_ab_y_disp(-phi8,P9a,0.,0.,0.)
##    P9a=dr.trans_xyz(P9a,0.0,0.0,-src.link_length.calf_right)
##    P9a=dr.rot_ab_y_disp(-phi7,P9a,0.0,0.0,0.)
##    P9a=dr.trans_xyz(P9a,0.0,0.0,-src.link_length.thigh_right)
##    P9a=dr.rot_ab_y_disp(-phi6,P9a,0.0,0.0,0.)
##    P9a=dr.trans_xyz(P9a,0.0,0.0,-src.link_length.hip_right)  #troublesome
##    P9a=dr.rot_ab_x_disp(theta5,P9a,0.0,0.0,0.)
##    P9a=dr.trans_xyz(P9a,0.,src.link_length.back,0.)
##    P9a=dr.rot_ab_x_disp(theta4,P9a,0.,0.,0.)
##    P9a=dr.trans_xyz(P9a,0.,0.,src.link_length.hip_left)
##    P9a=dr.rot_ab_y_disp(phi3,P9a,0.,0.,0.) 
##    P9a=dr.trans_xyz(P9a,0.,0.,src.link_length.thigh_left)
##    P9a=dr.rot_ab_y_disp(phi2,P9a,0.,0.,0.)
##    P9a=dr.trans_xyz(P9a,0.,0.,src.link_length.calf_left)
##    P9a=dr.rot_ab_y_disp(phi1,P9a,0.,0.,0.)
##    P9b=dr.trans_xyz(P9a,1.,0.,0.)
##    src.points_on_exo.P9.append(P9b)
##    
##    
##
    
    
    

