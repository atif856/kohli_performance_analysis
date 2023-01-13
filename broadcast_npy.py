import numpy as np

x = np.array([
    [2, 1, 3],
    [4, 3, 5],
    [7, 3, 8]
])

v = np.array([1, 0, 1])

# y = np.empty_like(x)
# print(y)

print(x)
print(v)


# ------------- 1st method -----------
# for i in range(len(x)):
#     y[i, :] = x[i, :] + v
# print(y)


# ------------- 2nd method ------------
# stacked_v = np.tile(v, (3,1))           #--> [[1, 0, 1]
# print(stacked_v)                        #     [1, 0, 1]
# print(x + stacked_v)                    #     [1, 0, 1]]


# -------------- using numpy ----------
y = x + v
print(y)


# -------- reshape the matrix ----------
y = np.array([
    [4, 5, 6],
    [1, 2, 0]
])
print(y)
print(y.shape)

z = np.reshape(y,(3,2))
print(z, z.shape)
