#COMPREHENSION: are way to create new sequence out of existing one
#four min types of comprehensions are : list comprehension, dictionary comprehension, set comprehension,generator comprehension

#let us see code example for each one by one

#LIST comprehension:
data_1=[10,8,3,4,5,6,9]
     #list comprehension:
data = [x+3 for x in data_1]  #updating list
     # Regular for loop:
for x in range(len(data_1)):
    data_1[x] = data_1[x] + 3
    #new list
new_data=[x*2 for x in data_1 if x%2==1]  #divisible by 3


#SET comprehension
set_a={x for x in range(10,20) if x not in [12,14]}
print(set_a)


#Dictionary comprehension
    #using range function and no input list
data_2={x:x*2 for x in range(12)}
print(data_2)
    #list
months=["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number=[1,2,3,4,5,6,7,8,9,10,11,12]
    #using one input list
numDict={x:x for x in number}
    #using two input lists
monthsDict={key:value for key, value in zip(number,months)}
print(monthsDict)


#Generator comprehension
    #similar to lists with variation of using curved brackets instead of square brackets
lis=[2,3,4,5,7]
gen_obj=(x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items)

