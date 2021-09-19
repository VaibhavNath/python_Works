# name='vaibhav'
# sur='nath'
# message=name+sur
# print(message)
# list=['a','b','v','i','p']
# print(sorted(list))
# print(list)

# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# #or

# squares=[i**2 for i in range(1,11)]
# print(squares)

# li=[]
# for i in range(1,1000001):
#     li.append(i)
    
# print(min(li))
# print(max(li))
# print(sum(li))


# cube=[i**3 for i in range(1,11)]              #list comprehension.
# print(cube)


# banned_user=['vivek','virat','pari']
# user='timtim'
# if user not in banned_user:
#     print(user.title()+" you can post")


# age = 85
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
# print(price)


# user_name=['vaibhav','devil','virat','admin','pari']
# # user_name=[]   # to make empty list
# if user_name:    # check for empty list,if list is empty then if block will not execute.
#     for user in user_name:
#         if user=='admin':
#             print('hello admin')
#         else:
#             print('hello ' + user +', good day')
# else:
#     print('list empty')



# alien_0={}
# alien_0['color']='green'
# print(alien_0)


# mydict={
#     'keyword':'reserved word',
#     'variable':'use to store value'
# }
# print(mydict.keys())
# for i in mydict:
#     a=input('enter word:\n')
#     print('\t',mydict.get(a))


# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() +", I see your favorite language is " + favorite_languages[name].title() + "!")


# import csv
# with open('protagonist.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer.writerow([2, "Harry Potter", "Harry Potter"])

# import re

# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	



# class Student:
#     __schoolName = 'XYZ School' # private class attribute

#     def __init__(self, name, age):
#         self.__name=name  # private instance attribute
#         self.__salary=age # private instance attribute
#     def __display(self):  # private method
# 	    print('This is private method.')

# std = Student("Bill", 25)
# print(std.__schoolName)


class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
del pt1
del pt2
del pt3