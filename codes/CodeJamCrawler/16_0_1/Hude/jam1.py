def decomp(n):
    if n >= 10:
        decomp(n / 10)
        decomp(n % 10)
    else:
        array[n] = True

T = int(raw_input())

inputs = []
for i in range(T):
    inputs.append(int(raw_input()))

i = 1
for N in inputs:
    n = N
    array = [False] * 10
    if n in [0]:
        print "Case #%s: %s"%(i, "INSOMNIA")
    else:
        while (1):
            decomp(n)
            if not False in array:
                break
            n += N;
        print "Case #%s: %s"%(i, n)
    i+=1