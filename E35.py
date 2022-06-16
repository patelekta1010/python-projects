import matplotlib
import matplotlib.pyplot as pt

fig = pt.figure()
rect = fig.patch
rect.set_facecolor('green')
x=[3,7,8,9]
y=[5,13,14,17]
x2=[0,4,7,10]
y2=[3,7,1,12]
x3=[2,4,6,8]
y3=[13,5,8,2]


graph1 = fig.add_subplot(2,2,1)
graph1.plot(x,y,'red',linewidth=2.0)
graph1.tick_params(axis="x",color="yellow")
graph1.tick_params(axis="y",color="yellow")
graph1.spines["top"].set_color('r')
graph1.spines["left"].set_color('r')
graph1.spines["right"].set_color('r')
graph1.spines["bottom"].set_color('r')
graph1.set_title('Random Graph', color='blue')
graph1.set_xlabel('This is the x axis',color='yellow')
graph1.set_ylabel('This is the y axis',color='yellow')


graph2 = fig.add_subplot(2,2,2)
graph2.plot(x2,y2,'yellow',linewidth=2.0)

graph2.tick_params(axis="x",color="yellow")
graph2.tick_params(axis="y",color="yellow")
graph2.spines["top"].set_color('r')
graph2.spines["left"].set_color('r')
graph2.spines["right"].set_color('r')
graph2.spines["bottom"].set_color('r')
graph2.set_title('Random Graph', color='blue')
graph2.set_xlabel('This is the x axis',color='yellow')
graph2.set_ylabel('This is the y axis',color='yellow')

graph3 = fig.add_subplot(2,1,2)
graph3.plot(x3,y3,'blue',linewidth=2.0)

graph3.tick_params(axis="x",color="yellow")
graph3.tick_params(axis="y",color="yellow")
graph3.spines["top"].set_color('r')
graph3.spines["left"].set_color('r')
graph3.spines["right"].set_color('r')
graph3.spines["bottom"].set_color('r')
graph3.set_title('Random Graph', color='blue')
graph3.set_xlabel('This is the x axis',color='yellow')
graph3.set_ylabel('This is the y axis',color='yellow')

pt.show()