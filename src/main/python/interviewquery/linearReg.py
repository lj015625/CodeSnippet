import numpy as np

A = [[1, 5], [4, 8], [5, 9]]
result = []
# for i in range(len(A[0])):
#     temp = []
#     for j in range(len(A)):
#         temp.append(A[j][i])
#     result.append(temp)
result = np.transpose(np.array(A))
print("A_T = ", result)  # calculating transpose using base python

X_b = np.array([[1, _] for _ in result[0]])
y = np.array([[_] for _ in result[1]])
print(X_b, y)
# Beta = (X^T X)^-1 X^T y
beta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print("Alpha = ", beta[1][0])
print("Beta = ", beta[0][0])
