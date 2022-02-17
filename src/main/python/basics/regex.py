import re

# 2 or more vowels between constants
a = re.findall('(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]', input(), re.I)
print('\n'.join(a or ['-1']))

# floating number
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

# first repeating alphnumeric
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)

# replace '&&' and '||' with 'and' and 'or'
N = int(input())
for i in range(N):
    # a look behind, and look forward with space
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))
    # remove comment
    print(re.sub("(<!--.*?-->)", "", input()))


# splitting numbers ex: 100,000,000.000
print("\n".join(re.split(r"[.,]+", input())))

# validate 9 digits phone number starting with 7 or 8 or 9.
n = int(input())
for i in range(n):
    if re.match(r'[789]\d{9}$', input()):
        print('YES')
    else:
        print('NO')

# validate zip code starting with 1-9 followed by 5 digits and end .
s = input()
print (bool(re.match(r'^[1-9][\d]{5}$',s) and len(re.findall(r'(\d)(?=\d\1)',s))<2 ))

# validate email address
n = int(input())
for _ in range(n):
    name, email = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email)
    if m:
        print(name, email)

# find substring pattern in string and output position
s = input()
sub = input()
pattern = re.compile(sub)
r = pattern.search(s)
if not r: print(tuple([-1,-1]))
while r:
    print(tuple([r.start(), r.end() - 1]))
    r = pattern.search(s, r.start() + 1)

# Roman numerals
thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"
regex_pattern = r"^" + thousand + hundred + ten + unit + "$"
print(str(bool(re.match(regex_pattern, input()))))

# UID
for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        # It must contain at least  uppercase English alphabet characters.
        assert re.search(r'[A-Z]{2}', u)
        #I t must contain at least  digits (0-9).
        assert re.search(r'\d\d\d', u)
        # It should only contain alphanumeric characters ( - ,  -  &  - ).
        assert not re.search(r'[^a-zA-Z0-9]', u)
        # No character should repeat.
        assert not re.search(r'(.)\1', u)
        # There must be exactly  characters in a valid UID.
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

