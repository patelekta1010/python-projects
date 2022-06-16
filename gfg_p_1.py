# ---------------------------write a Python program to swap first and last element of the list.-----------------------

x = [12,24,56,76,87,56,98]
print("original list :",x)
x[0], x[-1] = x[-1],x[0]
print("new list : ",x)
