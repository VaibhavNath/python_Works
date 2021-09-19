class Employee:     #create class
    company='google'     #methods of class
    def getsalary(self):    #use of self
        print(f'salary is {self.salary}')

Sam=Employee()    #object initialisation
Sam.salary=10000    #local declaration of salary
Sam.getsalary()  #or Employee.getsalary(Sam)

Sam.id='bt2589'
Employee.company='lens'  #changes the value of methods in class
print(Sam.company)

Sam.company='youtube'   #local declaration of company

print(Sam.company)
print(Sam.salary)
print(Sam.id)
