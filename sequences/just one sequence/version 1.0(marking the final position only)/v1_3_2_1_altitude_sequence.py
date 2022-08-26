import matplotlib.pyplot as plt
import numpy as np
import math

#************  OUTPUT PLOT PROPERTIES  ********#
fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection='3d')
ax.set_xlim([0,2.5])
ax.set_ylim([2.5,0])
ax.set_zlim([0,2.5])

#***********   INERTIAL REFERENCE FRAME ********#
ax.quiver(0,0,0,0,0,1.5)
ax.quiver(0,0,0,0,1.5,0)
ax.quiver(0,0,0,1.5,0,0)

#****** DEGRES TO RADIANS FUNCTION *******#
def degrees_to_radians(x):
    '''
    Converts degrees to radians since all operations in the math module are done in radians
    and the input of every trignometric function is in radians.
    '''
    return (x*math.pi)*(1/180)

#******  ROTATION MATRICES  ******#
def Cz(b):
    '''
    b=yaw angle.
    coordinate trasformation/rotation about z-axis.
    '''
    b = degrees_to_radians(b) #converting degrees to radians
    return np.array(
    [[math.cos(b), math.sin(b),0],
    [-math.sin(b), math.cos(b),0],
    [0,0,1]]
    )

def Cy(b):
    '''
    b=yaw angle.
    coordinate trasformation/rotation about z-axis.
    '''
    b = degrees_to_radians(b) #converting degrees to radians
    return np.array(
    [[math.cos(b),0, -math.sin(b)],
    [0,1,0],
    [math.sin(b),0 , math.cos(b)]]
    )

def Cx(b):
    '''
    b=yaw angle.
    coordinate trasformation/rotation about z-axis.
    '''
    b = degrees_to_radians(b) #converting degrees to radians
    return np.array(
    [[1,0,0],
    [0,math.cos(b), math.sin(b)],
    [0,-math.sin(b), math.cos(b)]]
    )

#*********   ORIGIN & IDENTITY MATRIX  ********#
zeros=[0.0,0.0,0.0]
I=np.array([[1,0,0],[0,1,0],[0,0,1]])

#*********  INPUTS(EULER ANGLES & NUMBER OF SEQUENCES)  **********#
print()
yaw_angle=int(input('Yaw angle  i.e., Cz(c), Psi in degrees: '))
print()
pitch_angle=int(input('Pitch angle  i.e., Cy(b), Theta in degreees: '))
print()
roll_angle=int(input('Roll angle  i.e., Cx(a), Phi in degrees: '))


final_position=I

def _3(final_position):
    q=None
    for a in np.linspace(0,-yaw_angle,30):
        frame=np.dot(Cz(a),final_position) #3


        q = ax.quiver(zeros,zeros,zeros,frame[0,:],frame[1,:],frame[2,:],color='r')
        plt.pause(0.003)
        if q:
            q.remove()
    return frame,q

final_position,q = _3(final_position)

def _3_2(final_position):
    q=None
    for a in np.linspace(0,-pitch_angle,30):
        frame=np.dot(Cy(a),final_position) #3

        q = ax.quiver(zeros,zeros,zeros,frame[0,:],frame[1,:],frame[2,:],color='r')
        plt.pause(0.003)
        if q:
            q.remove()
    return frame

final_position = _3_2(final_position)

def _3_2_1(final_position):
    q=None
    for a in np.linspace(0,-roll_angle,30):
        frame=np.dot(Cx(a),final_position) #3-2-1
        if q:
            q.remove()
        q = ax.quiver(zeros,zeros,zeros,frame[0,:],frame[1,:],frame[2,:],color='r')
        plt.pause(0.003)

    return frame

final_position = _3_2_1(final_position)


plt.show()  #if you want to see the final position of axes after rotation
print()
