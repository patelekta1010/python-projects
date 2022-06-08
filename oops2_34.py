class Employee:
    leaves= 8
    pass
ekta = Employee()
deep = Employee()
ekta.name="Ekta"
ekta.salary= 44400
ekta.role= "gamer"

deep.name = "Deep"
deep.salary = 34500
deep.role ="devops"
print(deep.leaves)
print(ekta.__dict__)
ekta.leaves= 6  #IT WILL NOT BE CHANGE... IT WILL CREATE A NEW INSTANCE
print(ekta.__dict__)
print(Employee.leaves)