#PURE FUNCTIONS:    make the code clean, better to debug,easier to read, and more consistent. There is difference between traditional function function and pure function. A pure function doesn't chane or have any effect on variables,data, list,sets present outside the function/beyond its own scope.
# eg, if you have a list of global scope, pure functtions cannot add into that list or alter it in any way. Following code have a function which is not pure:
global_list=[3,5,7];
def append_list(item):
    return global_list.append(item);

append_list(9);

print(global_list)

#Let us change this in pure function that doesn't change the actual global list instead make the copy of list and make changes to that copy an return the altered list.

global_list_2=[3,5,7];
def append_list_2(actual_list,item):
    x=actual_list
    return x.append(item);

append_list_2(global_list_2,0);
print(global_list_2)

#BENEFITS OF PURE FUNCTIONS:
# 1- Gives known output: You always know the output
# 2- Consistent and reliable: do exactly what they are intended to do
# 3- Cache: have ablity to cache since you already knnow te return is always going to be same.
# 4- Multi-threaded programs: lend themselves well to multithreaded program. In multi-threaded program, more than one process can run concurrently, which creates many threads of data.
# 5- Pure functions will help prevent changes of global scope assuring data state is reliable.