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

plt.show()
