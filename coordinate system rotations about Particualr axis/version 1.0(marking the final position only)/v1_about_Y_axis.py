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

zeros=[0.0,0.0,0.0]
q=None

print()
pitch_angle=int(input('Pitch angle i.e., theta in degreees: '))

for a in np.linspace(0,-pitch_angle,100):
    frame=Cy(a) #3
    if q:
        q.remove()

    q = ax.quiver(zeros,zeros,zeros,frame[0,:],frame[1,:],frame[2,:],color='r')
    plt.pause(0.003)

plt.show()  #if you want to see the final position of axes after rotation
