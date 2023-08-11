# 4 types of inheritance:

# SINGLE LEVEL INHERITANCE:
#    Enables derived class to inherit characteristics from single parent class

# MULTI LEVEL INHERITANCE:
#    Enables derived class to inherit properties from immediate parent class which in turn inherits properties from his parent class

# HIERARCHICAL INHERITANCE:
#   Enable more than one derived class to inherit properties from parent class

# MULTIPLE INHERITANCE:
#   Enable one derived class to inherit properties from more than one base class

class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber : {}".format(self.idnumber))


class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        pass

        self.post=post
        Person.__init__(self,name,idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

#object creation
a=Employee('IQRA',52,50000,"Intern")
a.display()
a.details()
print(a)


