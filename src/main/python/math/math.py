import cmath
# polar coordinates
print(*cmath.polar(complex(input())), sep='\n')

# divmod
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))

# power
a,b,c,d = (int(input()) for _ in range(4))
print (a**b+c**d)

# power of a to b, mod m
a,b,m = [int(input()) for _ in range(3)]
print(pow(a, b), pow(a, b, m), sep='\n')