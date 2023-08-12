#class method takes class as its implicit first argument 
class friends(object):
    @classmethod
    def study(cls):
        print("classmethod")

frd_1=friends()
frd_1.study()

#static method is not related to class or its instance, its like normal method as in procedural programming paradigm
#static method does not take implicit first argument, it may take its necessary arguments
class C(object):
    @staticmethod
    def fun( arg1, arg2):
        print("staticmethod")

c=C()
c.fun(2,3)


# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# A class method takes cls as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
#both return some method

#demonstrating class and static methods
from datetime import date 
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name,date.today().year-year)
    @staticmethod
    def isAdult(age):
        return age>18
    def simple_method(self,name,age):
        return self(name,age)
iqra = Person("Iqra",18)
irfu = iqra.fromBirthYear("irfu",2002)
# print(iqra.isAdult)
# print(iqra.simple_method())
# print(iqra.fromBirthYear("iqra",2003))
print(iqra.age)
print(irfu.age)
# POV: simple method in class can perform like static method too.
