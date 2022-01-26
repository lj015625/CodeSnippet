import numpy as np

# reshape
my_array = np.array([1,2,3,4,5,6])
print(np.reshape(my_array,(3,2)))
#Output
#[[1 2]
#[3 4]
#[5 6]]

# transpose and flatten
my_array = np.array([[1,2,3],
                        [4,5,6]])
print(np.transpose(my_array))
#Output
# [[1 4]
#  [2 5]
# [3 6]]

my_array = np.array([[1,2,3],
                        [4,5,6]])
print(my_array.flatten())
#Output
# [1 2 3 4 5 6]

print(np.transpose(my_array))
print(my_array.flatten())

# concatenate two arrays
array_1 = np.array([[1,2,3],[0,0,0]])
array_2 = np.array([[0,0,0],[7,8,9]])
print(np.concatenate((array_1, array_2), axis=1))
#Output
# [[1 2 3 0 0 0]
#  [0 0 0 7 8 9]]

# N * P array1
np_array1 = np.array([[1, 2],
                      [1, 2],
                      [1, 2],
                      [1, 2]])
# M * P array2
np_array2 = np.array([[3, 4],
                      [3, 4],
                      [3, 4]])
# (N+M) * P array
print(np.concatenate((np_array1, np_array2), axis=0))

# numpy arrays zeros and ones
print(np.zeros((1, 2)))                    #Default type is float
#Output : [[ 0.  0.]]
print(np.zeros((1,2), dtype = int))    #Type changes to int
#Output : [[0 0]]

# inner product(scalar)
A = np.array([0, 1])
B = np.array([3, 4])
print(np.inner(A, B))     #Output : 4

# outer product
A = np.array([0, 1])
B = np.array([3, 4])

print(np.outer(A, B))       #Output : [[0 0]
                            #          [3 4]]

# dot product
A = np.array([1, 2])
B = np.array([3, 4])
print(np.dot(A, B))    #Output : 11

# identity matrix and eye matrix
n, m = 3, 3
print(np.identity(3)) #3 is for  dimension 3 X 3
print(np.eye(n, m))

# math operations
a = np.array([1,2,3,4], float)
b = np.array([5,6,7,8], float)
print(a + b)                     #[  6.   8.  10.  12.]
print(np.add(a, b))           #[  6.   8.  10.  12.]

print(a - b)                     #[-4. -4. -4. -4.]
print(np.subtract(a, b))      #[-4. -4. -4. -4.]

print(a * b)                     #[  5.  12.  21.  32.]
print(np.multiply(a, b))      #[  5.  12.  21.  32.]

print(a / b)                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print(np.divide(a, b))        #[ 0.2         0.33333333  0.42857143  0.5       ]

print(a % b)                     #[ 1.  2.  3.  4.]
print(np.mod(a, b))           #[ 1.  2.  3.  4.]

print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(np.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]


# mean and std
my_array = np.array([ [1, 2], [3, 4] ])
print(np.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print(np.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
print(np.mean(my_array, axis = None))     #Output : 2.5

a1 = np.array([[2, 2],
               [1, 2],
               [3, 4]])
print(*(f for f in [np.mean(a1, axis=1), np.var(a1, axis=0), round(np.std(a1, axis=None), 11)]), sep='\n')

# floor ceil round nearest int
my_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(np.floor(my_array))         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

my_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(np.ceil(my_array))          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

my_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(np.rint(my_array))          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]


# max value of min value of columns
n, m=4,2
my_array = np.array([[2, 5],
                     [3, 7],
                     [1, 3],
                     [4, 0]])
print(np.max(np.min(my_array, axis=1)))

# the product of sum of two columns
my_array = np.array([ [1, 2], [3, 4] ])
print(np.sum(my_array, axis = 0))        #Output : [4 6]
print(np.sum(my_array, axis = 1))        #Output : [3 7]
print(np.sum(my_array, axis = None))     #Output : 10
print(np.sum(my_array))                  #Output : 10

my_array = np.array([ [1, 2], [3, 4] ])
print(np.prod(my_array, axis = 0))          #Output : [3 8]
print(np.prod(my_array, axis = 1))          #Output : [ 2 12]
print(np.prod(my_array, axis = None))       #Output : 24
print(np.prod(my_array))                    #Output : 24


# determinant, eigen vectors, values, inverse
print(np.linalg.det([[1 , 2], [2, 1]]))          #Output : -3.0

vals, vecs = np.linalg.eig([[1 , 2], [2, 1]])
print(vals)                                      #Output : [ 3. -1.]
print(vecs)                                      #Output : [[ 0.70710678 -0.70710678]
                                                 #          [ 0.70710678  0.70710678]]
print(np.linalg.inv([[1 , 2], [2, 1]]))          #Output : [[-0.33333333  0.66666667]
                                                 #          [ 0.66666667 -0.33333333]]

# The polyval tool evaluates the polynomial at specific value.
print(np.polyval([1, -2, 0, 2], 4))   #Output : 34