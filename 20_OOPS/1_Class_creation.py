#making empty class with no methods or attribute in it
#In python, class is not only a template but it is object itself, a class object, and many instances can be drawn from it which would then be called instance object.
class empty:
    pass;

#making dog class
class dog:
    print("this will execute at the time of instantiating the instance ")
    category="mammal";  # 1-attribute reference
    #constructor
    def __init__(self,name):
        self.name=name;
    def speak(self):
        print("my name is {}".format(self.name))
    def testing_class():
        print("run ")

#making object
small_dog=dog("Tom")  # 2-Instantiation

#There ae thrree types of object:
# 1- class object(dog)
# 2- Instance object(small_dog)
# 3- Method object(to access methods of the class)

#classes perform two types of operations:
# 1- Attribute references
# 2- Instantiation

#accessing attribute of obj
# print(small_dog.category)
# print(small_dog.name)

#The below two lines are same
small_dog.speak()
dog.speak(small_dog)
# print(dog.category)  #possible
# print(dog.name)      #not possible

#nstance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class. Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class

# we can change the vlaue of category for this instance or even the whole class
print(small_dog.category)
print(dog.category)
small_dog.category="not mammal"
print(small_dog.category)
print(dog.category) #not changed for class attribute
#let us change attribute for the whole class
dog.category="not mammal"
print(small_dog.category)
print(dog.category)
# congrats, changed
#is it changed for every instance? let us check
big_dog=dog("Jack")
print(big_dog.category) #yes, changed for every instance
dog.testing_class()