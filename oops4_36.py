class Employee:
    leaves= 8
    def __init__(self,aname,asalary,arole):
        self.name= aname
        self.salary=asalary
        self.role= arole

    def printdetails(self):
        return f" The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.leaves= newleaves

mummy= Employee("mummy",455,"instructor")
papa = Employee("Papa",255,"student")


mummy.change_leaves(34)
print(mummy.leaves)