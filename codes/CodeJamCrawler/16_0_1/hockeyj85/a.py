from __future__ import print_function

T = int(raw_input())

for t in range(T):
    print("Case #"+str(t+1)+": ", end='')
    
    n = int(raw_input())

    if n == 0:
        print("INSOMNIA")
        continue

    seen = {}
    k = 1;
    tn = n
    while len(seen) < 10:
        tn = n * k
        k += 1
        st = str(tn)
        for s in st:
            seen[s] = True
    print(str(tn))

