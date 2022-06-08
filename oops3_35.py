class Employee:
    leaves= 8
    def __init__(self,aname,asalary,arole):
        self.name= aname
        self.salary=asalary
        self.role= arole

    def printdetails(self):
        return f" The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

mummy= Employee("mummy",455,"instructor")
"""ekta = Employee()
deep = Employee()
ekta.name="Ekta"
ekta.salary= 44400
ekta.role= "gamer"

deep.name = "Deep"
deep.salary = 34500
deep.role ="devops"
print(ekta.printdetails())"""

print(mummy.salary)