# responsible for creating and returning new empty object
class recipe:
    def __new__(cls:type[self])->self:  #cls is not a keyword but a convention. it asks as a placeholder for passing the class as first argument which will be used for creating new empty object 
        pass
    def __init__(self)->None:
        pass

#init method takes the object created using new method along with other arguments, to initialize the other object being created 
    