#self represents the currrent instance of class 
# self and curent instance always points to same object

class check(object):
    def __init__(self):  #try by writing iqra instead of self
        print("Address of self = ",id(self))
        # print(self)

obj=check()
print("Address of class object = ",id(obj))
# print(obj)

#Self is first parameter in the methods of class, we can use another parameter too in place of self but it is always good practice to use self
