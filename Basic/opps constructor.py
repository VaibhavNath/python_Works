class Employee:     
    company='google' 

    def __init__(self,name,salary,subunit):    #constructor
        self.name=name
        self.salary=salary
        self.subunit=subunit        
        print('employee is created')

    def getdetails(self):
        print(f'name of employee is: {self.name} and salary is: {self.salary} in subunit: {self.subunit}')



vaibhav=Employee("vaibhav",100,"lens")    
vaibhav.getdetails()

