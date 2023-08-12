#static variable is class variable that is static/same for all instances of the class
#Instance variable is variable in class that vary instance to instance
#Static variables are defined inside the class definition, but outside of any method definitions.
#They are typically initialized with a value, just like an instance variable, but they can be accessed and modified through the class itself, rather than through an instance

class Person(object):
     class_variable_1="iqra"
     class_variable_2="meta"
    

p1=Person()
print(p1.class_variable_1)
p1.class_variable_1="irfu"
print(p1.class_variable_1)
