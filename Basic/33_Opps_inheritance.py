#single inheritence
class Employee:                #parent class
    company='google'

    def showDetails(self):
        print('this is an employee')

class Programmer(Employee):               #child class
    language='python'
    
    def getLanguage(self):
        print(f'the lang is {self.language}')

    def showDetails(self):
        print('this is an programmer')

a=Employee()
a.showDetails()
p=Programmer()
p.showDetails()
# print(p.company())
p.getLanguage()
Programmer.getLanguage='c'
print(p.getLanguage)