#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

lst = [56,34,25,91,45,32,56,87,95,76,12]
pos1 = 5
pos2 = 1
print("original list :",lst)
lst[pos1-1], lst[pos2-1] = lst[pos2-1], lst[pos1-1]

print("new list : ",lst)
