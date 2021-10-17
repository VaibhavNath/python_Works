list=[1,7,8,3,5,4,10]

# sorting of list(permanent)
list.sort()
print(list)

# reverse the list 
list.reverse()
print(list)

list.reverse()  #again reverse the list
print(list)

#append() adds to the end of list.
list.append(45)
print(list)

#insert (a,b) a=index,b=value
list.insert(0,544)
print(list)

list.insert(5,8990)
print(list)

#pop() removes index element
list.pop(3)
print(list)

#remove() removes the element
list.remove(8990)
print(list)
   

list=['a','b','v','i','p']
o=sorted(list)
print(o)      #temporary sort of list
o.reverse()     #reverse the list using sorted()   
print(o)
list.sort(reverse=True)     #reverse the list  with sorting
list.reverse()         #only reverse the list.
print(list)  


# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()    #pop last element of list.
# print(motorcycles)
# print(popped_motorcycle)



# list=['AYUSH','PRAKHAR','SNEHA']
# print('Your are invited to dinner,',list[0])
# print('Your are invited to dinner,',list[1])
# print('Your are invited to dinner,',list[2])

# print(list[1].capitalize(),'cannot arrive due to rain')
# list.remove(list[1])
# print(list)
# list.append('VARUN')
# print(list)
# print('Your are invited to dinner,',list[0])
# print('Your are invited to dinner,',list[1])
# print('Your are invited to dinner,',list[2])