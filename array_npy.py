# numpy array feature: (i) rank   (ii) shape   (iii) data type

import numpy as np

# ------ creating array of rank 1
# arr = np.array([1,4,5])

# print(arr)
# print("Type of array: ",type(arr))
# print("Shape of array: ",arr.shape)

# print(arr[0], arr[1], arr[2])

# arr[1]=10
# print(arr)

# ---- creating an array of rank 2 ------

# arr2D = np.array([
#     [2,5,6],
#     [1,5,3]
# ])

# print(arr2D)
# print(arr2D.shape)

# print(arr2D[0], type(arr2D[0]))
# print(arr2D[1], type(arr2D[1]))

# print(
#     arr2D[0, 0],
#     arr2D[0, 1],
#     arr2D[0, 2]
# )

# print(
#     arr2D[1, 0],
#     arr2D[1, 1],
#     arr2D[1, 2]
# )


# ------------------------------------------------------
# zeros = np.zeros((3,4))              # np.zeros((shape of the array/matrix))
# print(zeros, zeros.shape)

# ones = np.ones((4,5))
# print(ones, ones.shape)

# consts = np.full((3,7), 5)
# print(consts, consts.shape)

# random = np.random.random((4,4))
# print(random, random.shape)

# consts1 = np.full((4,4), 3)
# print(consts1)
# for i in range(3):
#     for j in range(3):
#         if(i==j):
#             consts1[i, j] = 0

# print(consts1)

# -----------------------------------

# temp = np.array([
#     [5,4,3,1],
#     [7,3,9,3],
#     [6,4,2,4]
# ])

# print(temp)

# s_arr = temp[:2, 1:3]
# print(s_arr)

# s_arr2 = temp[1:,2:]
# print(s_arr2)

# s_arr3 = temp[1,:]    # printing the whole row
# print(s_arr3)

# s_arr4 = temp[:,2]
# print(s_arr4)

# # print(temp[:2,:])

# print([temp>2])
# print(temp[temp>2])

x = np.array([[3,4], [7,6]], dtype=np.float64)
# print(x)
# print(x.dtype)

y = np.array([[2,5], [4,1]], dtype=np.float64)
# print(y)
# print(y.dtype)

print("Normal sum: \n", x+y)
print("Numpy sum: \n", np.add(x,y))

print("numpy subtract: \n",np.subtract(x, y))
print("numpy multiply: \n",np.multiply(x, y))
print("numpy divide: \n",np.divide(x, y))

print("numpy square root: \n",np.sqrt(x))


v = np.array([9,10])
w = np.array([5,6])

#  inner product
print(v.dot(w))
print(np.dot(v,w))

print(x.dot(v))
print(np.dot(x,v))

print(x.dot(y))

x = np.array([
    [1,2,3],
    [4,3,1],
    [5,8,3]
])
print(x)
print(x.T)      # transpose

print(np.sum(x))

print(np.sum(x, axis=0))           # column wise sum
print(np.sum(x, axis=1))           # row wise sum
