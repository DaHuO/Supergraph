import sys
for t in range(1, int(raw_input())+1, +1):
    idx = 1
    inputs = raw_input().split()
    K, C, S = inputs[0], inputs[1], inputs[2]
    for i in range(1, int(C), +1):
        idx *= int(K)
    sys.stdout.write('Case #' + str(t) + ': ')
    for i in range(0, int(S), +1):
        sys.stdout.write(str(idx*i+1)+' ')
    print ''
