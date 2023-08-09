#in python, there are generally 2 ways to handle files,
# text format      binary format

# 1- TEXT FORMAT:
#   more user friendly, Default format,

#2- BINARY FORMAT:
#   not user friendly, much more compact, better in performance
#   pass the letter 'b' along with mode(read or write or append mode)

with open("example.txt",mode='r+'):

#with open function is good at exception handling amd automatically closes the file
