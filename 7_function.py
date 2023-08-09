lis=[2,4,6,8,10];
def add(a):
    """
    the string enclosed in 3xdouble qoutes is documentation of function, that can be further accessed by using help command(method); i.e, help(<function name>)
    this function increase the value by one
    """
    return a+1
print(add(6));

def sum(lis):
    s=0
    for a in lis:
        s+=a;
    return s;

print(sum((4,6,7)))
print(sum([3,6,8]))

#for assigning return type to  python
def r(num1:int,num2:int):
    return "hello"
print(r(3,8)
)

#keyword argument
def k(a,b):
    return a,b
k(a=2,b=8)