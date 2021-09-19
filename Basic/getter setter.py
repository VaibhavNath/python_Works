class Employee:
    company='bharat gas'
    salary=4500
    salarybonus=600

    @property
    def totalSalary(self):
        return self.salary+self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val-self.salary


e=Employee()
print(e.totalSalary)
e.totalSalary=5600
print(e.salary)
print(e.salarybonus)
