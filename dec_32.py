#def function1():
 #   print("Ekta here")

#func2= function1
#del function1
#func2()

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
def who_is():
    print("ekta is good ")
who_is = dec1(who_is)
who_is()