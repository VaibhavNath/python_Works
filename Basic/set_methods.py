a={}   #retuns empty dict not empty set

b=set()  #returns an empty set
print(type(b))

b.add(4)
b.add(9)  #add elements to set b
print(b)

# b.add([4,5,6])   #error because list can't be added in set

b.add((4,5,6))    #tuple can be added in set
print(b)

# b.add({4:5})  #error because dict can't be added in set

print(len(b))   #prints length of set.

b.remove(9)   #removes the element from set.
# b.remove(15)   #throws an error while trying to remove 15(which is not present in set)
print(b)    

print(b.pop())   #removes any element from set and prints the removed element
print(b)

b.clear()  #clears the set
print(b)

