def solve(t):
    current = t[0]
    flips = 0
    for i in t:
        if i != current:
            current = i
            flips = flips + 1
    if current == '-':
        return flips + 1
    return flips

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        S = raw_input()
        print("Case #{0}: {1}".format(i+1, solve(S)))
