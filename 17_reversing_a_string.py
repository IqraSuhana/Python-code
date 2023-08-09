name="iqra"
marks=[89,34,12]

x=list(name)
x.reverse()
mane=""
for i in x:
    mane=mane+i
print(mane)




#    Using new variable and for loop
new=""
for i in range(0,len(name)):
    new=new+name[len(name)-1-i] #1 2
print(new)




#    Using FOR loop
let=""
for i in range(len(name)-1,-1,-1):
    let=let+name[i]
print(let)



#    Using SLICE function
print(name[len(name)-1::-1]) #or name[::-1]
# print(name)



#    Using RECURSION
def string_reverse_recursion(name):
    if len(name)==0:
        return name
    else:
        return string_reverse_recursion(name[1:])+name[0]
print(string_reverse_recursion(name))

#     Using filtered/map function

mane="iqra"
def reverse_str(char):
    # mane.append(char)
    return 

new_name=map(reverse_str,name)
# print(new_name)
for i in new_name:
    # print(i)
    pass