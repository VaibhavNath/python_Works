l=[1,7,9,8,78,88]
for i in l:
    print(i)


for i in range(8):     #prints value from 0 to 7
    print(i)


for i in range(1,8):     #prints value from 1 to 7
    print(i)



for i in range(1,8,2):     #prints value from 1 to 7 with escaping one value
    print(i)


#for with else statement
for i in range(5):
    print(i)
else:
    print('this is inside else of for')