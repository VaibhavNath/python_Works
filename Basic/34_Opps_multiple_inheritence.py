class Employee:
    company='gens'
    eCode=852

class Lancer:
    company='shoes'
    brand='sneakers'

class Programmer(Employee,Lancer):
    name='vaibhav'

p=Programmer()
print(p.name)
print(p.eCode)
print(p.company)
