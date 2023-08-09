

class Circle(object):
    def __init__(self,nam,age,field):
        print("hi")
         self.nam=nam
        global self.age=age
        global self.field=field
    def printing(self):
        print(name," is ",age," years old and studies ",field)


Small_circle=Circle()
Small_circle.printing()