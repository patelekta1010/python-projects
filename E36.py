import matplotlib.pyplot as pt
import numpy as np

x=["science","maths","physics"]
h=[200,250,400]
pt.bar(x,h,align='center',color='red')
pt.xlabel(' SUBJECTS',color="green")
pt.ylabel('SCORE',color="green")
pt.title('RESULTS',color='orange')
pt.tick_params(axis='x',colors='blue')
pt.tick_params(axis='y',colors='blue')
pt.show()
