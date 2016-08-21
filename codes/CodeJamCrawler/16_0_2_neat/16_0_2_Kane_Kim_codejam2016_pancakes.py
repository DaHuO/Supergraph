import fileinput


def find_last(lst, sought_elt):
    for r_idx, elt in enumerate(reversed(lst)):
        if elt == sought_elt:
            return len(lst) - 1 - r_idx
    return -1

def flip(inp, i):
    inp[:i+1] = list(reversed(map(lambda c: '-' if c == '+' else '+', inp[:i+1])))
    return inp

def solve(inp):
    inp = list(inp)
    count = 0
    l = len(inp)
    Found = False
    while not Found:
        for i, el in enumerate(inp):
            if el == '+':
                if i == l - 1:
                    return count
                n = inp[i+1]
                if n == "-":
                    inp = flip(inp, i)
                    count += 1
            else:
                try:
                    n = inp[i+1]
                    if n == "+":
                        inp = flip(inp, i)
                        count += 1
                except:
                    return count + 1
    return count

# print solve("-+")

for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    line = line.strip()
    res = solve(line)
    print "Case #%d: %d" % (i, res)
