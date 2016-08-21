T = int(raw_input())


def flip(pancakes, i):
    top = pancakes[:i]
    bottom = pancakes[i:]

    top = top[::-1].replace('-','*').replace('+','-').replace('*','+')

    return top + bottom

def solve(pancake):

    pancake = pancake.rstrip('+')

    if len(pancake) == 0:
        return 0

    c = 0
    sign = "-"
    while len(pancake) > 0:
        n = len(pancake) - len(pancake.rstrip(sign))
        if sign == "-":
            sign = "+"
        else:
            sign = "-"
        pancake = pancake[:len(pancake)-n]
        c += 1

    return c

for t in range(T):
    pancake = raw_input()
    print "Case #{}: ".format(t+1) + str(solve(pancake))
