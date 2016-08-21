import sys

T = input()

for t in range(1,T+1):
    N = input()
    
    if N == 0:
        print("Case #%d: INSOMNIA" % t)
        continue

    bitmap = 0
    M = 0 
    while True:
        M = M + N
        K = M
        while K:
            d = K % 10
            K = K / 10
            bitmap |= 1 << d

        if bitmap == 0b1111111111:
            print("Case #%d: %d" % (t, M))
            break 
