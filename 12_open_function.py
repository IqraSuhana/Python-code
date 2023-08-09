# #Creating new file and writing into them using 'w' mode
# #Not Creating new file for writing into it,instead, use existing file and writing into them using 'a' mode


# # store every line of file in the list as an element each

# # using 'w' mode, exixting file would be overwritten if exist
# #  using 'a' mode, existing file would remain and new text would be written after it called appending
# lines=["My name is IQRA IRFAN\n", "I am 18 years old.\n","I want to be tec specialist.\n","I want to marry with irfan sherani who is my love."]
# with open("WriteExample.txt",'w') as File1:
#     for line in lines:
#         File1.write(line);

# with open("WriteFile.txt",'w') as File1:
#     File1.writelines(["My name is iqra\n"," I am spouse of Irfan sherani"]);



# with open("Example.txt",'a') as File2:
#     for line in lines:
#         File2.write(line);

def read_file_into_list(file_name):
    with open(file_name,'a') as file:
       print(file.write("iqra"))

read_file_into_list("Example.txt")



    
