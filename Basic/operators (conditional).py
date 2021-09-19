age=int(input('enter age:\n'))
if(age>18 and age<34):
    print('young')
elif(age<18 and age>14):
    print('child')
elif(age<14 or age>34):
    print('not applicable')
else:
    print('false')


#else is optional
a=7
if(a==7):
    print('yes')
elif(a>56):
    print('yes and no')