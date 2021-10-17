class Person:
    def __init__(self):
        print('initialise person...')

    country='India'
    city='Gonda'
    def takeBreak(self):
        print('I am breating...')
    
class Employee(Person):
    def __init__(self):
        super().__init__()
        print('initialise employee..')
    company='honda'
    def getSalary(self):
        print(f'Salary is {self.salary}')

    def takeBreak(self):
        super().takeBreak()
        print('I am an employee...')

class Programmer(Employee):
    company='Lancer'

    def gerSalary(self):
        print('no salary')

    def takeBreak(self):
        super().takeBreak()
        print('I am an programmer...')

# p=Person()
# p.takeBreak()

e=Employee()
e.takeBreak()

# pr=Programmer()
# pr.takeBreak()