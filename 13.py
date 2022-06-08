list1=[ ["ekta",1],["deep",2],["taksh",3],["gopi",4]]
#print(list1)
dict1=dict(list1)
#print(dict1)
for item,rank in list1 :
    if rank<3 :
        print(item)