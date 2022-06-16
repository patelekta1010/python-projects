from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
import numpy as np

fig= pt.figure()

chart= fig.add_subplot(1,1,1,projection='3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[7,6,9,8,2,1,3,4,5,1]
z=[0,0,0,0,0,0,0,0,0,0]
dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

chart.bar3d(x,y,z,dx,dy,dz,color='cyan')

chart.set_xlabel('X-AXIS')
chart.set_ylabel('Y-AXIS')
chart.set_zlabel('Z-AXIS')
pt.show()