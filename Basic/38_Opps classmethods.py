class Employee:
    company='Camel'
    salary=100
    location="Gonda"
    # def changeSalary(self,sal):
    #     self.salary=sal

    @classmethod                       #changes the class attribute
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
print(Employee.salary)
e.changeSalary(455)               
print(e.salary)
print(Employee.salary)         #changes the class attribute
Employee.salary=200
print(Employee.salary)