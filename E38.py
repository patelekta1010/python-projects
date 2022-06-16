from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt


fig = pt.figure()
chart= fig.add_subplot(1,1,1,projection='3d')
x,y,z= [1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
xx,yy,zz= [-1,-2,-3,-4,-5,-6,-7,-8],[-2,-5,-3,-8,9,5,6,1],[-3,-6,-2,-7,-5,4,5,6]

chart.scatter(x,y,z,c='blue',marker='o')
chart.scatter(xx,yy,zz,c='green',marker='^')

chart.set_xlabel('X-AXIS')
chart.set_ylabel('Y-AXIS')
chart.set_zlabel('Z-AXIS')

pt.show()