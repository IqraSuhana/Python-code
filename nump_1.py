# 1-D array

# Python list allows us to store and access data,
#Numpy array is similar to the list,its fixed in size and each element is of same type

import numpy as np

a=np.array([1,2,3,5,7])
a[1]  #return 2
type(a)  #numpy.ndarray
a.dtype  #return datatype of array's elements; dtype('int64')
a.size  #return size of the array
#for higher dimensions
a.ndim   #return dimensions or rank of the array
a.shape    #tuple of integers indicating the size of the array for each dimensions

#for float type array
b=np.array([3.1,11.2,10,6.2,213,3])
type(b)  #numoy.ndarray
b.dtype  #dtype('float64')

#INDEXING
b[0]=34.6  #changing element of specific index of the array

#SLICING
d=a[2:4]    #d=array([1,2,3])

#assigning new values to corresponding indices
a[2,5]=4,6,8

#BASIC OPERATIONS
    #VECTOR ADDITION/SUBTRACTION
        #have applications in Data science
        u=[1,0]; v=[1,0];  #lists represents the vectors
        z=[]
        for n,m in zip(u,v):
        z.append(n+m)
    #VECTOR operation with 1 line numpy code
        u=np.array([1,0])
        v=np.array([0,1])
        z=u+v           #or z=u-v

    #vector multiplication with scalar
        y=np.array([1,2])
        z=2*y
#dot product of vectors
result=np.dot(u,v)
#adding constant to numpy array
    #broad casting is process of adding constant to each element of the array
z=u+3;

#UNIVERSAL FUNCTION:operates on n-d array
mean_of_a=a.mean();
max_b=b.max()
np.pi #pi symbol
x=np.array([0,np.pi/2,np.pi])
y=np.sin(x)

#function for plotting maths functions
np.linspace(-2,2,num=5)  #starting number,ending number,number of evenly spaced samples to generate
 
#library matplotlib.pyplot is helpful to plot functions
import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(x,y)




