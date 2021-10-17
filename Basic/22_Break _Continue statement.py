#for with else statement
for i in range(10):
    print(i)
    if i==5:
        break
else:
    print('this is inside else of for')    #else will execute only if for loop is successfully terminated else it wont get executed.



# #for with else statement
# for i in range(10):
#     if i==5:
#         continue          #for 5==5 it will continue and again go to for loop and will not print 5(5 will be skipped)
#     print(i)


# for i in range(10):
#     if i%2!=0:            #print only odd values.
#         print(i)


# for i in range(10):
#     if i%2==0:            #print only even values.
#         print(i)


# for i in range(10):
#     if i%2!=0:
#         continue            #print only even values.
#     print(i)