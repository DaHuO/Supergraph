cases = int(input())
def flip_c(cakes, start):
    for i in range(start,-1,-1):
        if cakes[i] == '-':
            cakes[i] = '+'
        elif cakes[i] == '+':
            cakes[i] = '-'
        else:
            print("wrong fmt!")
for i in range(cases):
    cakes = list(input())
    cl = len(cakes)
    flips = 0
    for k in range(cl-1,-1,-1):
        if cakes[k] == '-':
            flip_c(cakes, k)
            flips += 1
    print("Case #{}: {}".format(i+1, flips))
