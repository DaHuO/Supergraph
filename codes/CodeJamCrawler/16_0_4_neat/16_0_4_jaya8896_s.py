for cases in range(input()):
    k,c,s = map(int,raw_input().split())
    val = k
    for i in range(c-2):
        val = val*k
    val = k**(c-1)
    arr = [1]
    for i in range(k-1):
        arr.append(arr[-1]+val)
    print "Case #" + str(cases+1) + ": " + " ".join(map(str,arr))
