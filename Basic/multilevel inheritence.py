class Person:
    country='India'
    city='Gonda'
    def takeBreak(self):
        print('I am breating...')
    
class Employee(Person):
    company='honda'
    def getSalary(self):
        print(f'Salary is {self.salary}')

    def takeBreak(self):
        print('I am an employee...')

class Programmer(Employee):
    company='Lancer'

    def gerSalary(self):
        print('no salary')

    def takeBreak(self):
        print('I am an programmer...')

p=Person()
p.takeBreak()
e=Employee()
e.takeBreak()
p=Programmer()
p.takeBreak()

