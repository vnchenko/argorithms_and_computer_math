import numpy as np
from math import sqrt

print('_______12-variant_______\n')

A = [[3, 2, 1], [1, 12, 2], [1, 2, 3], [4, 2, 1]]
B = [3, 2, 1, 3]
number = 4

Aexample = [[1, 6, 1], [3, 7, 12], [5, 8, 13], [7, 9, 14], [9, 10, 5]]
Bexample = [5, 5, 5, 5, 5]

N = 5


U, S, V = np.linalg.svd(A)
S1 = np.matmul(np.diag(1 / S), np.eye(3, number))
print('Python:')
print(np.matmul(np.matmul(np.matmul(np.array(V).transpose(), S1),
                           np.array(U).transpose()), B))



print('                           ')

A_mul_AT = np.matmul(A, np.array(A).transpose())
eig_U = np.linalg.eig(A_mul_AT)[1]
eig_U[:, 2], eig_U[:, 3] = eig_U[:, 3], eig_U[:, 2].copy()
for i in [0, 2, 3]:
    eig_U[:, i] = -1*eig_U[:, i]
U_new = eig_U
# print(U_new)

# print(S)
S_new = []
S_eig = np.linalg.eig(A_mul_AT)[0]
for i in range(len(S_eig)):
    S_new.append(sqrt(abs(S_eig[i])))
S_new[2], S_new[3] = S_new[3], S_new[2]
S_new = S_new[:3]
AT_mul_A = np.matmul(np.array(A).transpose(), A)
eig_V = np.linalg.eig(AT_mul_A)[1].transpose()
for i in [0, 2]:
    eig_V[i, :] = -1*eig_V[i, :]
V_new = eig_V
# print(V_new)

S1 = np.matmul(np.diag(1 / np.array(S_new)), np.eye(3, number))

arr = np.matmul(np.matmul(np.matmul(np.array(V_new).transpose(), S1),
                           np.array(U_new).transpose()), B)

arr2 = []
for i in [0,1,2]:
    arr2.append(np.array(arr)[i] * -1)
print('Algorithm:\n', arr2)
print('                           ')
print('______CONTROL_EXAMPLE______\n')

U, S, V = np.linalg.svd(Aexample)
S1 = np.matmul(np.diag(1 / S), np.eye(3, N))

print("Python:\n", np.matmul(np.matmul(np.matmul(np.array(V).transpose(), S1),
                           np.array(U).transpose()), Bexample))

# print("U1",U)
A_mul_AT = np.matmul(Aexample, np.array(Aexample).transpose())
eig_U = np.linalg.eig(A_mul_AT)[1]

for i in [1, 3]:
    eig_U[:, i] = -1*eig_U[:, i]
eig_U[:, 3], eig_U[:, 4] = eig_U[:, 4], eig_U[:, 3].copy()
U_new = eig_U
# print("U_new",U_new)
# print()

# print("S1",S)
S_new = []
S_eig = np.linalg.eig(A_mul_AT)[0]
for i in range(len(S_eig)):
    S_new.append(sqrt(abs(S_eig[i])))
S_new[2], S_new[3] = S_new[3], S_new[2]
S_new = S_new[:3]
# print("S1", S1)
S_new = S1
# print("S_new",S_new)

# print("V1",V)
AT_mul_A = np.matmul(np.array(Aexample).transpose(), Aexample)
eig_V = np.linalg.eig(AT_mul_A)[1].transpose()
for i in [1, 2]:
    eig_V[i, :] = -1*eig_V[i, :]
eig_V[1, :], eig_V[2, :] = -eig_V[2, :], eig_V[1, :].copy()
eig_V[1, :] = -1*eig_V[1, :]
V_new = eig_V
# print("V_new",V_new)
X=np.matmul(np.matmul(np.matmul(np.array(V).transpose(), S1),
                           np.array(U).transpose()), Bexample)
X1=np.matmul(np.matmul(np.matmul(np.array(V_new).transpose(), S_new),
                           np.array(U_new).transpose()), Bexample)



print("\n\nAlgorithm:\n", X1)
