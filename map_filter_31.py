#_______________________map_______________________________
numbers = ["3","66","64"]

for i in range (len(numbers)):
    numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1
print(numbers[2])

numbers= list(map(int,numbers))
print(numbers)


def square(a) :
    return a*a
def cube(a):
    return a*a*a
func= [square, cube]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)


list_1 = [1,2,3,4,5,6,7,8,9]
#____________________filter___________________
def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5 , list_1))
print(gr_than_5)


#_____________________reduce_______________________
from functools import reduce
list1 = [1,2,3,4]
num= reduce(lambda x,y : x+y, list1)
print(num)