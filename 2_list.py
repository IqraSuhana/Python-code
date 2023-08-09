list_1=[3,2,1,"iqru"];
# print(list_1);
# print(*list_1)
# print(*list_1,sep='+')


list_2=list_1
list_2.insert(2,"irfan")
# print(list_2)
# print(list_1)


# since both variables are pointing towards same object(list),changing one variable will change other variable too
list_2[0]="procoder";
print(list_1);
list_2.extend(("hi extending",'023'));
list_1.extend(["hello extending",404])
print(list_2,'\n',list_1);

list_1.append(["appending","helo"])
list_2.append(('apend',400))
print(list_2,'\n',list_1);
list_1.pop(4)   #deleting
print(list_2,'\n',list_1);
del list_1[0]
print(list_2,'\n',list_1);


# print(list_2[3:8]);

# print("12787 hi".split());
# print(len(list_1))
