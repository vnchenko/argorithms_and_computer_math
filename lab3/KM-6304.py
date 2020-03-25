from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from math import exp

h = 0.1
a = 1
b = 2
y0 = -1
z0 = 0


def funct(u, x):
    y = u[0]
    z = u[1]
    return [z, 2*z + exp(x)]


x = np.arange(a, b+h, h)
beg = [y0, z0]
solution = odeint(funct, beg, x)

n = int((b - a) / h)
y = [[y0, z0]]

t = []
for i in range(0, n + 1):
    t.append(a + (i) * h)

for i in range(1, n + 1):
    temp = funct(y[i - 1], t[i - 1])
    y.append([y[i - 1][0] + h * temp[0], y[i - 1][1] + h * temp[1]])



plt.plot(x, solution[:, 0], 'b', label='theta(t)')
plt.plot(x, np.array(y)[:, 0], 'g', label='omega(t)')
print('dependencies x of y')
print(x, solution[:, 0])
print(x, np.array(y)[:, 0])
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

plt.plot(x, solution[:, 1], 'b', label='theta(t)')
plt.plot(x, np.array(y)[:, 1], 'g', label='omega(t)')
print('dependencies x of z')
print(x, solution[:, 1])
print(x, np.array(y)[:, 1])
plt.legend(loc='best')
plt.xlabel('tн')
plt.grid()
plt.show()
