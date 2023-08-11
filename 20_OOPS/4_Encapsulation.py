#Encapsulation is the process of making the variables and methods private to that class so that cannot be accessed by anyone in any way directly and change their value directly
#here we are making one variable c as private (encapsulated within its own class and not accessible by any one outside of this class)

class Base:
    def __init__(self):
        self.a="geeksforgeeks"
        self.__c="geeksforgeeks"
        print("Hi, I am base class")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)  #calling constuctor of parent class
        print(self.a)
        # print(self.__c) #cannot be accessed due to private access
        print("Hi, I am derived class")

#making object
obj=Base()
print(obj.a)
# print(obj.__c)  #we cannot access the variable c directly as it is private
child=Derived()