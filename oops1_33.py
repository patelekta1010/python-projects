#object - instance of class
#class -template

class Student:
    pass
ekta = Student()
deep = Student()
ekta.name = "Ekta"
ekta.std = "BE"
ekta.section = "CE "
deep.std ="ME"

print(ekta.section,deep.std)