import numpy as np

arr = np.random.uniform(low = 1, high = 20, size = (20,))

print (arr)

matrix = arr.reshape(5,4)

print()
print(matrix)

maxes = np.argmax(matrix, axis = 1)

matrix[0][maxes[0]] = 0
matrix[1][maxes[1]] = 0
matrix[2][maxes[2]] = 0
matrix[3][maxes[3]] = 0
matrix[4][maxes[4]] = 0
print()
print (maxes)
print ("replaced max values with 0: \n", matrix)