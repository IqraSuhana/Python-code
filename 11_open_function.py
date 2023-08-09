#open function is used to create a file object & obtain data from txt file

File1=open("Example.txt","w");
File1.write("this is file later explained with the keyword with. \n so let us start. ")
print(File1.name);
print(File1.mode);
File1.write("another line in example.txt file")
# print(File1.read());  #.read() will not run for 'w' mode specified file
File1.close()
File=open("Example.txt",'r');
print(File.read())
# File.write("another line in example.txt file")     #.write() will not run for 'r' mode specified file

# Using 'with' statement,opening the file is better practice bcs it automatically closes the file
#  .readlines() method will read the file as it is, without counting the separate lines, instead print '\n' in place of new line.
# so using .read() will be acceptable and convenience in this circumstances
 
with open("Example.txt",'r') as File2:
    file_stuff=File2.read()
    print(file_stuff);

# print(File2.read())  #content can't be read outside indented block
print(file_stuff);   #content can't be read outside indented block, but variable (in which content is stored) can be read
print(File2.closed); #check if file closed

with open("Example.txt",'r') as File3:
    # file_stuff_1=File3.readlines()   #return list of lines of File3
    #if above 1 line code run first,remaining 6 line code will create problem
    # print(file_stuff_1)
    file_line=File3.readline();         #1st call, return 1st line 
    print(file_line)
    file_line=File3.readline();         #2nd call, return 2nd line , and so on
    print(file_line)
    file_line=File3.readline(5);        #3rd call, return 5 characters of 3rd line   
    # file_line=File3.readline(4);        #return next 4 characters than previous

# print(file_stuff_1)
# print(file_stuff_1[1])   #print 1st line only
print(file_line)


with open("Example.txt",'r') as File4:
        file_stuff_2=File4.readline(1)  #return 1 character
        file=File4.readline(3)          #return 3(next) character
#         #the character/portion/word of the file that is already read will not be read again, instead next part will be read by next read() type function. This is Proved by above example
print(file_stuff_2)
print(file)



