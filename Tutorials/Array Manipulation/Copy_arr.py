'''
Method 1: Using np.empty_like() function
This function returns a new array with the same shape and type as a given array.
numpy.empty_like(a, dtype = None, order = ‘K’, subok = True)
'''

import numpy as np

ary = np.array([13, 99, 100, 34, 65, 11,  
                66, 81, 632, 44])
print("Original array: ", ary)

# Creating an empty Numpy array similar to ary
copy= np.empty_like(ary)

# now assigning ary to copy
copy[:] = ary

print(copy) 

'''
Method 2: Using np.copy() function

This function returns an array copy of the given object.
and you can also create a copy of any dimensional array
'''

org_array = np.array([1.54, 2.99, 3.42, 4.87, 6.94, 
                      8.21, 7.65, 10.50, 77.5]) 

print(org_array)

# now copying array using np.copy() function
copy_array= np.copy(org_array)
print(copy_array)   # in this method you don't need to create an empty array after that assign the values