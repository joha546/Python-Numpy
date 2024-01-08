# importing numpy module
import numpy as np

# creating list 
list = [1, 2, 3, 4]

# creating numpy array
sample_array = np.array(list)

print("List in python : ", list)

print("Numpy Array in python :",sample_array)

# creating list 
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

# creating numpy array
sample_array = np.array([list_1, 
						list_2,
						list_3])

print("Numpy multi dimensional array in python\n",
	sample_array)


print(sample_array.shape)

print(sample_array.dtype)

b= np.array((1,2,3), dtype=float)
print(b)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)