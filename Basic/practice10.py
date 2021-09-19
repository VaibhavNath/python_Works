# class Programmer:
#     company='Microsoft'
#     def __init__(self,name,product,salary):
#         self.name=name
#         self.product=product
#         self.salary=salary    

#     def getdetails(self):
#         print(f'name of the {self.company} programmer employee is: {self.name} and product is: {self.product} with salary: {self.salary}')

# vaibhav=Programmer("Vaibhav","AI",52000)
# vaibhav.getdetails()
# isha=Programmer("Isha",'Machine Learning',65000)
# isha.getdetails()



# class Calculator:
#     def __init__(self,num):
#         self.number=num
#     def Square(self):
#         print(self.number **2)
#     def Cube(self):
#         print(self.number **3)
#     def CubeRoot(self):
#         print(self.number**0.5)

# a=Calculator(16)
# a.Square()       
# a.Cube()
# a.CubeRoot()



# class Sample:
#     a='vaibhav'

# obj=Sample()
# obj.a='nath'
# Sample.a='nath'   #this will change the class attribute.
# print(Sample.a)
# print(obj.a)




# class Calculator:
#     def __init__(self,num):
#         self.number=num
#     def Square(self):
#         print(self.number **2)
#     def Cube(self):
#         print(self.number **3)
#     def CubeRoot(self):
#         print(self.number**0.5)
#     @staticmethod
#     def greet():
#         print('*****Good Morning , Sir*****')
    

# a=Calculator(16)
# a.greet()
# a.Square()       
# a.Cube()
# a.CubeRoot()


# class Train:
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
    
#     def getStatus(self):
#         print(f'The name of the train is {self.name} with fare Rs.{self.fare} and number of seats {self.seats}')
    
#     def booktickets(self):
#         if(self.seats>0):
#             print(f'Ticket booked with seat number {self.seats}')
#             self.seats=self.seats-1
#         else:
#             print(f'Sorry train if full,kindly try in tatkaal')


# interCity=Train("Intercity express:14015",352,2)
# interCity.getStatus()
# interCity.booktickets()  #books 1seat
# interCity.booktickets()   #books 2 seat
# interCity.booktickets()   #prints sorry message
# interCity.getStatus()



class Sample:
   
    def __init__(vaibhav,name):
        vaibhav.name=name

obj=Sample('vaibhav')
print(obj.name)
