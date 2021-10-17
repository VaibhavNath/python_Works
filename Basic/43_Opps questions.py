#codesdope.com :- python practice questions on object oriented programming.


'''1.
Create a Cricle class and intialize it with radius.
Make two methods getArea and getCircumference inside this class.'''

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return 3.14*self.radius*self.radius

    def getCircumference(self):
        return 2*3.14*self.radius

'''2.
Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''

class Temperature:
    def farh(self,cel):
    return (cel * (9/5)) + 32

    def cel(self,farh):
        return (farh-32)*(5/9)

'''3.
Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.'''

class Student:
    def __init__(self,anme,rollNo):
        self.name=name
        self.rollNo=rollNo
    
    def setAge(self,age):
        self.age=age

    def setMarks(self,marks):
        self.marks=marks
    
    def display(self):
        print self.name
        print self.rollNo
        print self.age
        print self.marks

'''4.
Create a Time class and initialize it with hours and minutes.
1. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
2. Make a method displayTime which should print the time.
3. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.'''

class Time:
    def __init__(self,hours,min):
        self.hours=hours
        self.min=min

    def addTime(t1,t2):
        t3=Time(0,0)
        if t1.min+t2.min>60:
            t3.hours=(t1.min+t2.min)/60
        t3.hours=t3.hours+t1.hours+t2.hours
        t3.min=(t1.min+t2.min)-(((t1.min+t2.min)/60)*60)
        return t3

    def displayTime(self):
        print(f'time is {self.hours} hours and {self.min} minutes.')
    
    def DisplayMinute(self):
        print(self.hours*60)+self.min

a=Time(2,50)
b=Time(1,20)
c=Time.addTime(a,b)
c.displayTime()
c.DisplayMinute


# 5.Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self,maxSpeed,mileage):
        self.maxSpeed=maxSpeed
        self.mileage=mileage

modelIx=Vehicle(100,50)
print(modelIx.maxSpeed,modelIx.mileage)


# 6.Create a Vehicle class without any variables and methods
class Vehicle:
    pass