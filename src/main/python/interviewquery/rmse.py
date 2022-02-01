import math

def calculate_rmse(y_pred, y_true):
    sum = 0
    n = len(y_pred)
    for i in range(n):
        sum += (y_true[i] - y_pred[i])**2

    return math.sqrt(sum/n)

y_pred = [3,4,5]
y_true = [3,4,5]

print(calculate_rmse(y_pred, y_true))