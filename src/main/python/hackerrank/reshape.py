import numpy

arr = list(map(int, input().split()))
my_array = numpy.array(arr)
print(my_array.reshape(3,3))
