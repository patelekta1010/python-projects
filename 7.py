#dictionary : it is a key value pairs
d1={}
print(type(d1))
d2={"Ekta":"ice cream","Rutvi":"aloo paratha","Khushi":"roti"
    ,"deep":{"b":"egg","l":"roti","d":"milk"}}
print(d2["deep"]["b"])
d2["megha"]="pizza"
d2[876]="maggie"
print(d2)
del d2[876]
d3=d2
print(d2.copy())
d2.update({"gopi":"chocolate"})
print(d2.keys())
print(d2.items())
m="""hjjjygyhgh"""
print(m)