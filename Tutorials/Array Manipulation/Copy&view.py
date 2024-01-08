'''Normal assignments do not make the copy of an array object. Instead, it uses the exact same id of the original
array to access it. Further, any changes in either get reflected in the other.'''

import numpy as np

arr = np.array([2,4,6,8])

#assigning array to nc
nc=arr

# both arr and nc have same id
print(id(arr))
print(id(nc))

nc[0]=12

print(arr)
print(nc)

'''
  Output
id of arr 26558736
id of nc 26558736
original array-  [12  4  6  8 10]
assigned array-  [12  4  6  8 10]   This is also known as Shallow Copy
'''

# View\
'''ndarray. view() helps to get a new view of array with the same data. 
    Syntax: ndarray.view(dtype=None, type=None)
    '''
    
arr1 = np.array([8, 10, 12, 14, 16])

# creating view
v=arr1.view()

# both arr and v have different id 
print("id of arr", id(arr1)) 
print("id of v", id(v)) 

# changing original array 
# will effect view 
arr1[0] = 12

''' Output
id of arr 30480448
id of v 30677968
original array-  [12  4  6  8 10]
view-  [12  4  6  8 10]    This is also known as Deep Copy. The copy is completely a new array and copy owns 
the data
'''

'''
To check whether array own it’s data in view and copy we can use the fact that every NumPy array has the attribute
base that returns None if the array owns the data. Else, the base attribute refers to the original object.
'''

print(arr.base)
print(nc.base)
