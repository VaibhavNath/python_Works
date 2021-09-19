f1=input('enter fruit number 1: ')
f2=input('enter fruit number 2: ')
f3=input('enter fruit number 3: ')
f4=input('enter fruit number 4: ')
f5=input('enter fruit number 5: ')
f6=input('enter fruit number 6: ')
f7=input('enter fruit number 7: ') 
myFruitList=[f1,f2,f3,f4,f5,f6,f7]
print(myFruitList)


marks1=int(input('enter the marks of student 1: '))
marks2=int(input('enter the marks of student 2: '))
marks3=int(input('enter the marks of student 3: '))
marks4=int(input('enter the marks of student 4: '))
marks5=int(input('enter the marks of student 5: '))
marks6=int(input('enter the marks of student 6: '))
marksOfStudents=[marks1,marks2,marks3,marks4,marks5,marks6]
marksOfStudents.sort()
print(marksOfStudents)

list=[4,8,3,5]
print(list[0]+list[1]+list[2]+list[3])   #individual add of all elements
print(sum(list))    #sum methods all over

t=(0,4,0,5,8,0,36,0,89,7)
print(t.count(0))