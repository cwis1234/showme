
import numpy as np

A = np.array([[5,3,4,7,0],[5,7,8,9,1],[0,1,88,4,7]])
B = np.array([7,5,10])
print(A)
print(B.T)
U,s,V = np.linalg.svd(A,full_matrices = True)
S = np.zeros(A.shape)
for i in range(len(s)):
	S[i][i] = 1/s[i]

A_ = np.dot(V,np.dot(S.T,U.T))
print(A_)
x = np.dot(A_,B)
print(x)