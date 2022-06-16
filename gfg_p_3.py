'''Given a string. the task is to check if the string is symmetrical and palindrome or not.
A string is said to be symmetrical if both the halves of the string are the same
and a string is said to be a palindrome string if one half of the string is the reverse of the other half
or if a string appears same when read forward or backward.'''

stg = "ammamma"

half = int(len(stg)/2) # dividing the string in to two parts

if len(stg)% 2 == 0 :#even
    first_stg = stg[:half]
    second_stg = stg[half:]
else:#odd
    first_stg = stg[:half]
    second_stg = stg[half+1:]
#symmetric
if first_stg == second_stg :
    print("The string is symmetrical")

else:
    print("The string is not symmetrical")

#palindrome
if first_stg == second_stg[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")






