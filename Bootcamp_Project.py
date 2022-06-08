# PROJECT  FOR BOOTCAMP IN PYTHON AND NETWORK SECURITY
#PROJECT:   WRITE A PROGRAM IN PYTHON TO GENERATE MD5 OF STRING DATA.

import hashlib

# initializing string
ekta=input("Enter a string :")

#ENCODING THE INPUTED STRING USING encode()
# then sending to md5()
result = hashlib.md5(ekta.encode())

# printing the equivalent hexadecimal value.
print(" the generated MD5 of string data is : ", end="")
print(result.hexdigest())