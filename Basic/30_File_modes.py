# f=open('another.txt','w')    #creates a file with name another.txt if the file does not exists 
# f.write('please write again in file')   #creates file with this line written in file.  
# f.close()


# f=open('another.txt','a')    #appends a file   
# f.write('please write again in file')   #writes the line at the end of file
# f.close()


# f=open('another.txt','w')    #open the file in write mode
# f.write(' write again in file')   #replaces the content of file if the file already exist(and is not blank file) and we open in write  
# f.close()


with open('another.txt','r')as f:    #here we dont need tO close the file,file get closed automatically
    a=f.read()
with open('another.txt','w')as f:
    a=f.write('me very good boy')
print(a)   #prints the length of all words present in file
