#def function_name_print(a, b, c, d):
#   print(a, b, c, d)

#function_name_print("ekta", "deep", "taksh", "vilka")


def funargs(normal, *args, **kwargs) :
    print(type(args))
    print(normal)
    for item in args :
        print(item)
    print("\nNow I would like to introduce my family ")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


var = ["ekta", "deep", "taksh", "vilka"]
normal= "this is normal"
kw= {"papa" : "family head", "deep" :"study boy","ekta" : "lazy girl", "mumma" : " working women"}
funargs(normal, *var,**kw)
