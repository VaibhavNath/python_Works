mydict={
    'fast':'in a quick manner',
    'marks':[1,2,3],
    'anotherdict':{'vaibhav':'good boy'},
    1:2
}

#dictionary methods

print(mydict.keys())  #returns the keys of dict

print(type(mydict))   #class of dict

print(list(mydict))  #typecasting dict to list

print(mydict.values())  #returns the values of dict

print(mydict.items())    #returns the keys,values for all contents of dict

updateDict={            #update or add key and values to dictionary
    4:5
}
mydict.update(updateDict)
print(mydict)

del mydict[1]    #delete key-value pair from dictionary.
print(mydict)

print(mydict.get("fast"))  #returns value associated with key 'fast'
print(mydict['fast'])   #returns value associated with key 'fast'

#difference between .get and []syntax in dict

print(mydict.get("fast2"))  #return none as fast2 is not present in dict
# print(mydict['fast2'])   #returns error as fast2 is not present in dict 



