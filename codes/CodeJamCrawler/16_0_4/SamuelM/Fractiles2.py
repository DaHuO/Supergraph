t = int(input()) 
for i in range(1, t + 1):
    k,c,s = [int(s) for s in input().split(" ")]
    L = []
    while s != 0:
        L.append(s)
        s -= 1
    L.reverse()
    sr = ''
    for st in L:
        sr += str(st) + ' '
    print("Case #{}: {}".format(i, sr))
        