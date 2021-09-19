class Employee:     #create class
    company='google'     #methods of class
    def getsalary(self,signature):    #use of self
        print(f'salary is {self.salary}\n{signature}')

    @staticmethod          #static method declaration.here we dont need to pass arguement
    def greet():
        print('good morning,sir')
    @staticmethod
    def time():
        print('time is 10:00am')

Sam=Employee()    #object initialisation
Sam.salary=10000    #local declaration of salary
Sam.getsalary('thanks')    #by this signature is called in def
# vaibhav.getsalary()  #or Employee.getsalary(Sam)
Sam.greet()
Sam.time()