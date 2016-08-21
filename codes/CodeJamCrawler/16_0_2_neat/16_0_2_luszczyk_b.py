def simplify(string):
    last = '+'
    num = 0
    for digit in reversed(string):
        if digit == last:
            pass
        else:
            last = digit
            num += 1
    return num


assert simplify("") == 0
assert simplify("-") == 1
assert simplify("+") == 0
assert simplify("++--++-+") == 4

def read_ints():
    return map(int, input().strip().split())

n, = read_ints()
for case in range(n):
    s = input()
    num = simplify(s)
    print("Case #{}: {}".format(case + 1, num))
