import matplotlib
import matplotlib.pyplot as pt
x= []
y= []
readFile = open("example.txt","r")
data = readFile.read().split("\n")
for i in data:
    val = i.split(",")
    x.append(int(val[0]))
    y.append(int(val[1]))
pt.plot(x,y)
print(data)
print(x)
print(y)
#pt.plot([1,2,3,4],[3,8,10,25])
#pt.title('Rain in November')
#pt.xlabel('Days in November')
#pt.ylabel('Inches of Rain')
pt.show()
