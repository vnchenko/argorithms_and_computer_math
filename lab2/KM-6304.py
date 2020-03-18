import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# #
# Y = [0, 1.18, 1.9, 2.33, 2.59]
# X= [0, 1, 2, 3, 4]

X = [0, 1, 2, 3, 4, 5]
Y = [1.2, 3.7, 4.8, 14.2, 24.1, 58.5]

n = len(X)

F = []
SumF = 0

for i in range(n-1):
    F.append(np.log((Y[i+1]-Y[i])/(X[i+1]-X[i])))
    SumF = SumF + F[i]
print(F)

Xt = []
SumXt = 0

for i in range(n-1):
    Xt.append((X[i+1]+X[i])/2)
    SumXt = SumXt + Xt[i]
print(Xt)

Xt2 = []
SumXt2 = 0

for i in range(n-1):
    Xt2.append((Xt[i])**2)
    SumXt2 = SumXt2 + Xt2[i]
print(Xt2)

XF = []
SumXF = 0

for i in range(n-1):
    XF.append(Xt[i]*F[i])
    SumXF = SumXF + XF[i]
print(XF)

A = np.array([[n-1, SumXt], [SumXt, SumXt2]])
b = np.array([SumF, SumXF])

solve = np.linalg.solve(A, b)
print(solve)

Bk = -solve[1]
print(Bk)

Ak = np.exp(solve[0])/Bk
print(Ak)

Yt = []
SumY = 0

for i in range(n):
    Yt.append(Ak*(1 - np.exp(-Bk*X[i])))
    SumY = SumY + (Y[i] - Yt[i])


Ck = SumY/n
print(Ck)

def exp_func(x, a, b, c):
    return a *(1 - np.exp(-b * x)) + c

Y_exp = []
for i in X:
    Y_exp.append(exp_func(i, Ak, Bk, Ck))


SumError = 0
for i in range(1, n):
    SumError = SumError + np.fabs((Y[i]-Y_exp[i])/Y[i])
Abs_error = 100*SumError/(n-1)
print('Approximation error: ', round(Abs_error,5),'%')

plt.scatter(X,Y)
plt.plot(np.arange(0, 5.1, 0.1), exp_func(np.arange(0, 5.1, 0.1), Ak, Bk, Ck), color = 'g', label="external")
# plt.show()




def func_exp(x, a, b, c):
    # c = 0
    return a * np.exp(b * x) + c



if n==6:
    def exponential_regression(x_data, y_data):
        popt, pcov = curve_fit(func_exp, x_data, y_data)
        # popt, pcov = curve_fit(func_exp, x_data, y_data, p0=(-1, 0.01, 1)
        print(popt)
        puntos = plt.plot(x_data, y_data, 'x', color='xkcd:maroon', label="data")
        curva_regresion = plt.plot(x_data, func_exp(x_data, *popt), color='xkcd:teal',
                                   label="internal: {:.3f}, {:.3f}, {:.3f}".format(*popt))
        plt.legend()
        plt.show()
        return func_exp(x_data, *popt)


    exponential_regression(np.array(X), np.array(Y))

else:
    def exponential_regression1(x_data, y_data):
        popt, pcov = curve_fit(func_exp, x_data, y_data, p0=(-1, 0.01, 1))
        print(popt)
        puntos = plt.plot(x_data, y_data, 'x', color='xkcd:maroon', label="data")
        curva_regresion = plt.plot(x_data, func_exp(x_data, *popt), color='xkcd:teal',
                                   label="internal: {:.3f}, {:.3f}, {:.3f}".format(*popt))
        plt.legend()
        plt.show()
        return func_exp(x_data, *popt)
    exponential_regression1(np.array(X), np.array(Y))
