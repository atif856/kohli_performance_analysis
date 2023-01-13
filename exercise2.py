import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)     # (lower limit, higher limt, no of values)
print(x)

def func(x):
    y = []
    for elem in x:
        result = 5*elem**2 + 6*elem +3
        y.append(result)
    return y

y = func(x)

plt.plot(x, y)
plt.show()