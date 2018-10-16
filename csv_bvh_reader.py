# this is used for reading in the converted data from the perception neuron
# and then output the info or something
import csv
import math
import sensor_reader_class as src
import matplotlib.pyplot as plt
import Lower_Body_Calculations as LBS
import loc_of_foot_half as lofh
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import savgol_filter
import pandas as pd
joint_loc_rot_dic = {}

with open ('Matt_lift_2_Char00.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
   
    for row in csv_reader:
        joint_loc_rot_dic[row[0]] = row[1:]

Hip_Offset = [0.0, 95.729,0.0]

#print (joint_loc_rot_dic['LeftHandZrot'][200])

ax = Axes3D(plt.figure(1))
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.axis("equal")

HipAngX = []
HipAngY = []
HipAngZ = []

KneeAngX = []
KneeAngY = []
KneeAngZ = []

AnkleAngX = []
AnkleAngY = []
AnkleAngZ = []

time = []

for x in range(int(len(joint_loc_rot_dic['Frames'])-1)):
    time.append(float(joint_loc_rot_dic['Frames'][x]) / 120)
        
    HipAngX.append((float(joint_loc_rot_dic['LeftUpLegXrot'][x])))
    HipAngY.append((float(joint_loc_rot_dic['LeftUpLegYrot'][x])))
    HipAngZ.append((float(joint_loc_rot_dic['LeftUpLegZrot'][x])))

    if(x>=1):
        LBS.JointAngleCheck(HipAngX,HipAngY,HipAngZ)
        
    KneeAngX.append((float(joint_loc_rot_dic['LeftLegXrot'][x])))
    KneeAngY.append((float(joint_loc_rot_dic['LeftLegYrot'][x])))
    KneeAngZ.append((float(joint_loc_rot_dic['LeftLegZrot'][x])))
    
    AnkleAngX.append((float(joint_loc_rot_dic['LeftFootXrot'][x])))
    AnkleAngY.append((float(joint_loc_rot_dic['LeftFootYrot'][x])))
    AnkleAngZ.append((float(joint_loc_rot_dic['LeftFootZrot'][x])))
        
    src.angles_on_exo.LeftAnkle.append(math.radians(float(joint_loc_rot_dic['LeftFootZrot'][x])))
    src.angles_on_exo.LeftKnee.append(math.radians(float(joint_loc_rot_dic['LeftLegXrot'][x])))
    src.angles_on_exo.LeftHip.append(math.radians(float(joint_loc_rot_dic['LeftUpLegZrot'][x])))
    
    lofh.loc_of_foot(float(src.angles_on_exo.LeftAnkle[-1]),float(src.angles_on_exo.LeftKnee[-1]),
                          float(src.angles_on_exo.LeftHip[-1])) #,float(joint_loc_rot_dic['HipsXpos'][x]),
                         # float(joint_loc_rot_dic['HipsZpos'][x]),float(joint_loc_rot_dic['HipsYpos'][x]))
    XVals = [src.points_on_exo.Hips[x][0].item(0),src.points_on_exo.HipLeft[x][0].item(0), src.points_on_exo.LeftKnee[x][0].item(0), src.points_on_exo.LeftAnkle[x][0].item(0), src.points_on_exo.LeftFoot[x][0].item(0)]        
    YVals = [src.points_on_exo.Hips[x][1].item(0),src.points_on_exo.HipLeft[x][1].item(0), src.points_on_exo.LeftKnee[x][1].item(0), src.points_on_exo.LeftAnkle[x][1].item(0), src.points_on_exo.LeftFoot[x][1].item(0)]      
    ZVals = [src.points_on_exo.Hips[x][2].item(0),src.points_on_exo.HipLeft[x][2].item(0), src.points_on_exo.LeftKnee[x][2].item(0), src.points_on_exo.LeftAnkle[x][2].item(0), src.points_on_exo.LeftFoot[x][2].item(0)]     

    ax.plot(XVals,YVals,ZVals)
#print(HipAngY)
#print(joint_loc_rot_dic['LeftUpLegYrot'])
LeftAnkleAng = pd.DataFrame(src.angles_on_exo.LeftAnkle)    
LeftAnkleAng.rolling(window=3).mean()  

LeftKneeAng = pd.DataFrame(src.angles_on_exo.LeftKnee) 
LeftKneeAng.rolling(window=3).mean()

LeftHipAng = pd.DataFrame(src.angles_on_exo.LeftHip)
LeftHipAng.rolling(window=3).mean()

plt.figure(3)
plt.plot(time,LeftAnkleAng, time ,LeftKneeAng, time, LeftHipAng)


plt.figure(2)
plt.subplot(3,1,1)    
plt.plot(time, HipAngX, time, HipAngY, time, HipAngZ) #, time, HipAngXhat)
plt.title('Hip Angle Versus Time ')
plt.xlabel('time (s)')
plt.ylabel('Hip Ang (deg)')
plt.grid(True)
plt.legend(['X','Y','Z','XFiltered'], loc = 'lower left')

plt.subplot(3,1,2)
plt.plot(time, KneeAngX, time, KneeAngY, time, KneeAngZ)
plt.title('Knee Angle Versus Time ')
plt.xlabel('time (s)')
plt.ylabel('Knee Ang (deg)')
plt.grid(True)
plt.legend(['X','Y','Z'], loc = 'lower left')

plt.subplot(3,1,3)
plt.plot(time, AnkleAngX, time, AnkleAngY, time, AnkleAngZ)
plt.title('Ankle Angle versus Time ')
plt.xlabel('time (s)')
plt.ylabel('Ankle ANgle (deg)')
plt.grid(True)
plt.legend(['X','Y','Z'], loc = 'best')






#print (src.angles_on_exo.LeftAnkle)
    
## Create cubic bounding box to simulate equal aspect ratio
#max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
#Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(XVals.max()+XVals.min())
#Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(YVals.max()+YVals.min())
#Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(ZVals.max()+ZVals.min())
## Comment or uncomment following both lines to test the fake bounding box:
#for xb, yb, zb in zip(Xb, Yb, Zb):
#   ax.plot([xb], [yb], [zb], 'w')
#
#plt.grid()
#plt.show()