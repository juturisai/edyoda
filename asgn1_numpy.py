import numpy as np

# 1. Create a null vector of size 10 but the fifth value which is 1.
np_array = np.zeros(10)
np_array[4] = 1
print(np_array)

#2.Create a vector with values ranging from 10 to 49.
np_array = np.arange(10,50)
print(np_array)


#3. Create a 3x3 matrix with values ranging from 0 to 8
np_array = np.arange(0,9)
np_array = np_array.reshape((3,3))
print(np_array)

#4. Find indices of non-zero elements from [1,2,0,0,4,0]
np_array = np.array([1,2,0,0,4,0])
print(np_array.nonzero())

#5. Create a 10x10 array with random values and find the minimum and maximum values.
np_array = np.random.random((10,10))
print('min',np_array.min())
print('max',np_array.max())


#6. Create a random vector of size 30 and find the mean value.
np_array = np.random.random(30)
print('mean',np_array.mean())
