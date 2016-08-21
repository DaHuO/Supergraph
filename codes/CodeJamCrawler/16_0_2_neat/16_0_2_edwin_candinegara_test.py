T = int(input())

def isDone(l):
    for i in l:
        if not i:
            return False

    return True

def flip(l, index):
    for i in range (0, index + 1):
        l[i] = not l[i]

    return l

def solve(l):
    count = 0

    for i in range (len(l) - 1, -1, -1):
        if isDone(l):
            break
        
        if not l[i]:
            l = flip(l, i)
            count += 1

    return count

for i in range (0, T):
    S = input()
    l = [True if s =='+' else False for s in S]

    result = solve(l)
    print("Case #{}: {}".format(i + 1, result))
