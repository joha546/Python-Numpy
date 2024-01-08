import numpy as np
 
# creating an array
arr = np.array([1, 8, 3, 3, 5])
print(arr)

arr=np.append(arr,[7])
print(arr)

'''
Output 
Original Array :  [1 8 3 3 5]
Array after appending :  [1 8 3 3 5 7]
'''

# Appending Another Array at the End of a 1D Array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3=np.append(arr1,arr2)
print(arr3)

'''
Appending Using List Comprehension and numpy.concatenate
In this example, multiple arrays, including arr and two arrays from values_to_append, are concatenated using 
list comprehension and np.concatenate(), producing a single combined array.
'''

arr4= np.array([1,2,3,4,5,6])

values_to_append=[np.array([7,8]), np.array([9,10])]
combined= np.concatenate([arr4] + values_to_append)
print(combined)



# Appending Values at the End of the N-Dimensional Array
# It is important that the dimensions of both the array matches otherwise it will give an error.

aray= np.array(1,13).reshape(2,6)
print(aray,'\n')

# create another array which is to be appended column-wise.
col=np.arange(5,11).reshape(1,6)
print(col)

arr_col = np.append(aray,col, axis=0)  # here axis=0 represents to be worked on column or y axis
print(arr_col)

# create an array which is to be appended row-wise
row= np.array([1,2]).reshape(2,1)
print(row)
arr_row= np.append(aray,row, axis=1)
print(arr_row)