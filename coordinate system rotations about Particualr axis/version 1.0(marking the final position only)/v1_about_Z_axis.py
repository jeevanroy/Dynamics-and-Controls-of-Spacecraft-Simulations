import matplotlib.pyplot as plt
import numpy as np
import math


fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection='3d')
ax.set_xlim([0,2.5])
ax.set_ylim([2.5,0])
ax.set_zlim([0,2.5])

ax.quiver(0,0,0,0,0,1.5)
ax.quiver(0,0,0,0,1.5,0)
ax.quiver(0,0,0,1.5,0,0)

def degrees_to_radians(x):
    '''
    Converts degrees to radians since all operations in the math module are done in radians
    and the input of every trignometric function is in radians.
    '''
    return (x*math.pi)*(1/180)


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

zeros=[0.0,0.0,0.0]
q=None

print()
yaw_angle=int(input('Yaw angle i.e., psi in degrees: '))

for a in np.linspace(0,-yaw_angle,100):
    frame=Cz(a) #3
    if q:
        q.remove()

    q = ax.quiver(zeros,zeros,zeros,frame[0,:],frame[1,:],frame[2,:],color='r')
    plt.pause(0.003)

plt.show()  #if you want to see the final position of axes after rotation
