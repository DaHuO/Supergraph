def flip(s):
    if s[0] == '+':
        return (''.join((reversed(s[:(s+'-').find("-")])))).translate(str.maketrans('+-','-+')) + s[(s+'-').find("-"):]
    else:
        return (''.join((reversed(s[:(s+'+').find("+")])))).translate(str.maketrans('+-','-+')) + s[(s+'+').find("+"):]

def f(s):
    count = 0
    while not all(c == '+' for c in s):
        count += 1
        s = flip(s)
    return count

T = int(input())

for i in range(T):
    print("Case #{}: {}".format(i + 1, f(input().strip())))
