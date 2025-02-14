import numpy as np
import matplotlib.pyplot as plt

h = 1
k = 3

r = 3

def x(t):
    return h + r * np.cos(t)

def y(t):
    return k + r * np.sin(t)

plt.figure(figsize=(8, 8))
t_values = np.linspace(0, 2 * np.pi, 100)
x_values = x(t_values)
y_values = y(t_values)
plt.plot(x_values, y_values, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circle with center (1, 3) and radius 3')
plt.grid(True)
plt.legend()
plt.show()
