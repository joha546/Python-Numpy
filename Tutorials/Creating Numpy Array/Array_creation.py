'''Array creation using List : Arrays are used to store multiple values in one single variable.Python does not have 
built-in support for Arrays, but Python lists can be used instead.'''

arr = [1,2,3,4,5]
for i in arr:
    print(i)
    
# Array creation using array functions 
import array

arr= array.array('i',[1,2,3,4,5])  # syntax = array(datatype,value liset)
for i in range(0,3):
    print(arr[i],end=" ")
    
print('\r')

import numpy as np

a= np.empty([3,3])
print(a)