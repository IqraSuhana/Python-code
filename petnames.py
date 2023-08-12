#comverting file content into list

import random

with open("petnames.txt",'r') as pet:
    file_content=pet.read()
    file_content_list=file_content.split('\n')
    print(file_content_list)
    print(random.choice(file_content_list))