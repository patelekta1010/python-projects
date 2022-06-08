import math
me="EKTA"
a1=3
a="this is %s %s"%(me,a1)
print(a)

b="This is {1} {0}"
c=b.format(me,a1)
print(c)

#   FAST   ....fstring
d=f"This is {me} {a1} {3*6} {math.cos(65)}"
print(d)