import matplotlib.pyplot as pt

size=[50,23,7,15,5]
labels=['Android','Apple','Windows','Blackberry','Xiomi']
colors=["yellow","orange","cyan","magenta","red"]
pt.pie(size,colors=colors,startangle=90,labels=labels)
pt.title("PIE CHART")
pt.legend(title='Legend')
pt.axis('equal')
pt.legend(title='Legend',loc='lower left')

pt.show()
