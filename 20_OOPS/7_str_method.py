#python has special method that show how a particular object should be reperesented as string in python.
#It gives an object a human readable textual representation which is helpful for logging, debugging or showing users object information.
#When class object is used to create a string using built-in functions print() and str(), the __str__() function is automatically used
#We can alter how objects of class are represented in strings by defining the __str__() method

class GFG(object):
    def __init__(self,name,company):
        self.name=name
        self.company=company

    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."
    
my_intro=GFG("Iqra","META")
print(my_intro)