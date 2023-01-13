import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y = x**2
y1 = 5*x**2 + 6*x +3
y2 = 1 - ((x**2)/2)

# creating first subplot
plt.subplot(2, 1, 1)            # (height, width, active=1(active)/0(not active))
plt.plot(x, y_sin)
plt.title("Sine wave")

# creating second subplot
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title("Cosine wave")

# plt.subplot(5, 1, 3)
# plt.plot(x, y)
# plt.title("y=x**2 curve")

# plt.subplot(5, 1, 4)
# plt.plot(x, y1)
# plt.title("equation curve")

# plt.subplot(5, 1, 5)
# plt.plot(x, y2)
# plt.title("3rd curve")


# # plt.plot(x, y)                   # y = x**2


# # plt.plot(x, y1)                  # y = 5"x**2 + 6*x + 3

# plt.plot(x, y2)                    # y = 1 - ((x**2)/2)



# creting plot for both sine and cosine in one graph

# plt.plot(x, y_sin)
# plt.plot(x, y_cos)

# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("sine and cosine")
# plt.legend(["Sine", "Cosine"])
plt.show()

# print(x)
# print("\n")
# print(y)
