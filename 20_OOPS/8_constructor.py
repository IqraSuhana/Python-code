# 2 types -->parameterized  non-parametrized/default

#default
class hi(object):
    def __init__(self):
        print("hi")

#parametrized
class Add(object):
    first=0;
    second=0
    result=0
    def display(self):
        print("Addition is :"+str(self.result))
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def calculate(self):
        self.result=self.first+self.second

obj1=Add(2,5)
obj1.calculate()
obj1.display()

#we can make one constuctor that can be both parametrized and non parametrized

class class3:
    def __init__(self,name=None):
        if name is None:
            print("Default constructor called")
        else :
            print("Parameterized constructor called")

obj2=class3("")