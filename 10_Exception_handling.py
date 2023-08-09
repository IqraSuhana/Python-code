#Exception occurs at the time of code execution, can be handled by developer
#1.
try:
    print("hi");
    x=7
    x.append();
except:
    print("this is the exception error occured")

#2.

# we can make except statement more specific by including base class exception right after except
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)

#OR

try:
     x=2/0
except Exception as e: #where e is alias for exception
     #we can also replace this base class 'Exception' with the actual error, say 'zeroDivisionError', to make the exception feedback more specific
     print("something went wrong!",e)
     print(e.__class__) #we can also access actual type/class of exception that's occured.
    #or

#3.

items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except IndexError as e:
    print("this index doesnt exist!",e)

#4. 
#for more than one execption

try:
     getfile=open("myfile",'r')
     getfile.write("my file for exception handling.");
     print("hi hello",2/0)  # last except will run if above lines are all errorless   
except IOError:  # execute if IO error occurs, otherwise not...
     print("Unable to open or read the data in the file.");
except: #not good practice bcs reason/detail not specified
     print("Some other error occured!");
else:  #if no error occurs...
     print("the file was written successfully.")
finally:  #run in every condition
     # getfile.close(); 
     print("file is now closed.")