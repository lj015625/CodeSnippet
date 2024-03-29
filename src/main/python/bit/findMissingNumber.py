"""Bitwise operation to find missing number O(1) space and O(n) time. """
def find_missing(full, missing):
    m = 0
    # XOR 0 ^ 1 = 1
    for i in full:
        m ^= i

    # 1 ^ 1 = 0 
    for i in missing:
        m ^= i

    return m

f = [-1000, 1000, 400, 5]
miss = [-1000, 1000, 400]

print(find_missing(f, miss))