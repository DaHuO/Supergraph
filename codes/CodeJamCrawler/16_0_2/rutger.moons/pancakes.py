__author__ = 'rutger'


def convert_stack(s):
    b = [False] * len(s)
    for i in range(len(s)):
        b[i] = s[i] == "+"
    return b


def flip_stack(x):
    for i in range(len(x)):
        x[i] = not x[i]
    return x, 1

def flip_front_plus(x):
    flippedSomething = False
    counter = 0
    for i in range(len(x)):
        if x[i]:
            x[i] = False
            flippedSomething = True
        else:
            break
    if flippedSomething:
        counter = 1
    return x, counter

def trim_stack(s):
    x = s
    while len(x) > 0:
        if x[-1]:
            x = x[:-1]
        else:
            break
    return x


def getNbFlips(s):
    count = 0
    x = s   #x is trimmed
    while len(x) > 0:
        x, flipCounter = flip_front_plus(x)
        count += flipCounter
        x, flipCounter = flip_stack(x)
        count += flipCounter
        x = trim_stack(x)
    return count


def solve(s):
    x = convert_stack(s)
    x = trim_stack(x)
    if len(x) == 0:
        return 0
    else:
        return getNbFlips(x)


T = int(input())
for t in range(T):
    stack = input()
    result = solve(stack)
    print("Case #%d: %d" % (t + 1, result))
