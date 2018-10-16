# creating a class to store global variables for the exo
# IMU Class
class IMU_class:
    A1X = []
    A1Y = []
    A1Z = []
    A2X = []
    A2Y = []
    A2Z = []
    A3X = []
    A3Y = []
    A3Z = []  

    def __init__(self):
        A1X = []
        A1Y = []
        A1Z = []
        A2X = []
        A2Y = []
        A2Z = []
        A3X = []
        A3Y = []
        A3Z = []
# IMU time class
class IMU_time_class:
    t_A1X = []
    t_A1Y = []
    t_A1Z = []
    t_A2X = []
    t_A2Y = []
    t_A2Z = []
    t_A3X = []
    t_A3Y = []
    t_A3Z = []  

    def __init__(self):
        t_A1X = []
        t_A1Y = []
        t_A1Z = []
        t_A2X = []
        t_A2Y = []
        t_A2Z = []
        t_A3X = []
        t_A3Y = []
        t_A3Z = []

#Force Sensor Class
class Force_class:
    F1 = []
    F2 = []
    F3 = []
    F4 = []
    F5 = []
    F6 = []
    F7 = []
    F8 = []

    def __init__(self):
        F1 = []
        F2 = []
        F3 = []
        F4 = []
        F5 = []
        F6 = []
        F7 = []
        F8 = []
#Force Sensor TIme Class
class Force_time_class:
    t_F1 = []
    t_F2 = []
    t_F3 = []
    t_F4 = []
    t_F5 = []
    t_F6 = []
    t_F7 = []
    t_F8 = []

    def __init__(self):
        t_F1 = []
        t_F2 = []
        t_F3 = []
        t_F4 = []
        t_F5 = []
        t_F6 = []
        t_F7 = []
        t_F8 = []

#Angle Reading Class Lists
class Angle_class:
    A1 = []
    A2 = []
    A3 = []
    A4 = []
    A5 = []
    A6 = []

    def __init__(self):
        A1 = []
        A2 = []
        A3 = []
        A4 = []
        A5 = []
        A6 = [] 
        
#Angle Reading Time Class
class Angle_time_class:
    t_A1 = []
    t_A2 = []
    t_A3 = []
    t_A4 = []
    t_A5 = []
    t_A6 = []

    def __init__(self):
        t_A1 = []
        t_A2 = []
        t_A3 = []
        t_A4 = []
        t_A5 = []
        t_A6 = []


# Class to store linkage of EXO data
class link_length:
    calf_left = 100.0
    calf_right = 100.0
    thigh_left = 100.0
    thigh_right = 100.0
    hip_left = 100.0
    hip_right = 100.0
    back = 100.0
    foot = 25

# Current measured angles for calculations

class meas_ang_class:
    hipL = 0.0
    hipR = 0.0
    kneeL = 0.0
    kneeR = 0.0
    AnkleL = 0.0
    AnkleR = 0.0

class cent_mass_links:
    foot_L=[]
    calf_L=[]
    thigh_L=[]
    hip_L=[]
    back_=[]
    hip_R=[]
    thigh_R=[]
    calf_R=[]
    foot_R=[]

class points_on_perception:
    Hips = []
    RightUpLeg = []
    RightLeg= []
    RightFoot = []
    LeftLegUp = []
    LeftLeg = []
    LeftFoot = []
    Spine = []
    Spine1 = []

class angles_on_exo:
    Hips = []
    RightFoot = []
    LeftFoot = []
    RightAnkle = []
    LeftAnkle = []
    RightKnee = []
    LeftKnee = []
    RightHip = []
    LeftHip = []
    Spine = []
    Spine1 = []

class points_on_exo:
    Hips = []
    HipLeft = []
    HipRight = []
    RightFoot = []
    LeftFoot = []
    RightAnkle = []
    LeftAnkle = []
    RightKnee = []
    LeftKnee = []
    Spine = []
    Spine1 = []

class Center_of_Mass:
    COM_Foot_L=0.5
    COM_Calf_L=0.5
    COM_Thigh_L=0.5
    COM_Torso=0.5
    Total_COM=[]

class mass_segments:
    calf_left = 10.0
    calf_right = 10.0
    thigh_left = 15.0
    thigh_right = 15.0
    torso = 200.0
    foot_left = 7.0
    foot_right = 7.0
    
    
    


