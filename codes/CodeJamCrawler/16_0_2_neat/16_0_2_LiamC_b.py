def flip(x):
    return "-" if x == "+" else "+"
t = int(input())
for case in range(1,t+1):
    p = list(input())
    n = 0
    for i in reversed(range(len(p))):
        if p[i] == "+":
            continue
        else: # need to fill rear
            j = 0
            while p[j] == "+":
                j += 1
            if j: # have to flip front
                for k in range(j):
                    p[k] = flip(p[k])
                n += 1
            for k in range(i+1):
                p[k] = flip(p[k])
            n += 1
    print ("Case #{}: {}".format(case, n))
