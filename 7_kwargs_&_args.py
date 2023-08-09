#args and kwargs are arguments passed to function in more model manner

# ARGS:
#When number of element the function would accept is not confirm, then we use args,like:

def sum(*args):
    sum=0
    for x in args:
        sum+=x;
    return sum;

print(sum(3,5))
print(sum(2,7.7,9))

#KWARGS:
#KeyWord args

def add(**kwargs):
    mult=0
    for k,v in kwargs.items():
        mult+=v
    return mult;

print(add(juice=2,cake=4.5,coffee=1))



#summary: we can pass any amount of non keyword variables/arguments with args
#summary: we can pass any amount of keyword arguments with kwargs