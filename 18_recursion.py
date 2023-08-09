# Specially good for working on things that have many possible branches and :  Repetitive problems         Complex structure
#e.g, Searching through a file system
#Reursion is smilar to for-loop
# In recursion, we should always consider the results on prior basis otherwise it will convert to an infinite loop
#
#
#
#
# Consider the example of calculating the factorial
#        By LOOPing Method
def find_factorial_by_looping(n):
    if n<0:
        return 0;
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact;
print(find_factorial_by_looping(6))


#         By RECURSION Solution
def find_factorial_by_recursion(n):
    if n<0:
        return 0
    elif (n==1 or n==0):
        print("n is ",n)
        return 1
    else:
        return n*find_factorial_by_recursion(n-1)
        
print(find_factorial_by_recursion(4))
    
