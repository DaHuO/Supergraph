import sys

def pancake(p):
    if all([i == 1 for i in p]):
        return 0
    res = []
    for i in range(1, len(p)):
        c = p
        c = [-x for x in c[:i:-1]] + c[i:]
        res.append(1 + pancake(c))
    return min(res)

#print(pancake([-1,1,-1]))


def pancake2(p):
    count = 0
    for i in range(len(p) -1):
        # print(p)
        if p[i] != p[i+1]:
            # print('in if {}'.format(i))
            p = [-x for x in p[:i+1]][::-1] + p[i+1:]
            count += 1
        # print(p)
    if all([i == +1 for i in p]):
        return count
    return count +1

filename = sys.argv[1]

with open(filename) as f:
    f.readline()
    i = 1
    for line in f:
        line = line.strip()
        p = [1 if x == '+' else -1 for x in line]
        print("Case #{}: {}".format(i, pancake2(p)))
        i += 1

