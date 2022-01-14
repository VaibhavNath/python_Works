# use open function to read content of a file

# f=open('Z_sample.txt','r')
# f=open('Z_sample.txt')   #by default the mode is r=read
# data=f.read(8)    #read first 8 characters from file
# print(data)
# f.close()

# readline.file

f=open('Z_sample.txt')  
data=f.readline()    #read only one line from file.
print(data)

# data=f.readline()    #read second line from file.
# print(data)
# f.close()