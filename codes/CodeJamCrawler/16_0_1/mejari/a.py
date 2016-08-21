f = open("A-large.in", 'r')
T = int(f.readline())
for t in range(T):
    n = int(f.readline())
    if(n == 0):
        print("Case #" + str(t+1) + ": INSOMNIA")
    else:
        digits = [0,0,0,0,0,0,0,0,0,0]
        count = 0
        k = 1
        kn = n
        while(count < 10):
            kn = n*k
            arr = str(kn)
            for e in arr:
                if(digits[int(e)] == 0):
                    digits[int(e)] = 1
                    count += 1
            k += 1
        print("Case #" + str(t+1) + ": " + str(kn))
