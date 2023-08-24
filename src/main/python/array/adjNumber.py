# Write a Python function that adds together all combinations of adjacent integers of a given string of integers named int_str.

def int_str_addition(int_str):
    sum = 0
    for i in range(len(int_str)):
        for j in range(i+1, len(int_str)+1):
            # print(int(int_str[i:j]))
            sum += int(int_str[i:j])
    return sum

# 1+2+12+123+2+23+3
print(int_str_addition('123'))
