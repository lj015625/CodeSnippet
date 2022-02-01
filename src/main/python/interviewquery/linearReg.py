import numpy as np
import matplotlib.pyplot as plt

# generate x and y
x = np.linspace(0, 1, 10)
y = 1 + x + x * np.random.random(len(x))
# assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T
# turn y into a column vector
y = y[:, np.newaxis]

AT = np.transpose(np.array(A))
print("A_T = ", AT)  # calculating transpose using base python
# X_b = np.array([[1, _] for _ in AT[0]])
# y = np.array([[_] for _ in AT[1]])
# print(X_b, y)

# (A^T A)^-1 A^T y
coefficients = np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)
print(coefficients)
print("Alpha = ", coefficients[1][0])
print("Beta = ", coefficients[0][0])

alpha = np.dot(coefficients, y)
# plot the results
plt.figure(figsize=(10, 8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
