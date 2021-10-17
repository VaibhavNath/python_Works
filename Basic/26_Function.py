# def add(a,b):
#     return a+b 

# s=add(5,6)
# print(s)


# #quiz
# def greet(name):
#     print('Good Day, '+name)
# greet('Vaibhav')


def greet(name='stranger'):   #we define function with name'stranger'so that if function is called w/o arguement,it may not result in error.
                                            # it is called default parameter value
    print('Good Day, ' + name)

greet('Vaibhav')
greet()      #does not return error as no arguement is passed






