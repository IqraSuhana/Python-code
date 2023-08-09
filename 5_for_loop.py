#range function outputs an ordered sequence as a list
#if input is positive integer, he output is sequence that contains the same number of element as the input, eg; range(12) will return the list having integers from zero(0) to eleven(11) 
print(range(12))
#or
print(range(0,12))

#  FOR LOOP

#many of the procedures cant be used on tuples,so focus on lists here
for i in range(0,3):
    print(i)
    print("hi")

list_1=[23,34,56,69]

for i in list_1:
     print(i)

#enemurate is the function used to access the  elements of the list according to index
for index,element in enumerate(list_1):
    print(element)
    print(index)

print(i)