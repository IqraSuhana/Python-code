# Use to process a list
str_list=["pizza","burgur","coffee","Biryani","Noodles"]



def find_food(food):
    if(food[0]=='c'):
        return food;

#     map function
map_return=map(find_food,str_list)
print(map_return)
for x in map_return:
    print(x)

#     filtered function
filter_return=filter(find_food,str_list)
print(filter_return)
for x in filter_return:
    print(x)