for T in range(int(input())):
    n = int(input())
    l = ""

    for i in range(2*n-1):
        l += input() + " "
    l = list(map(int, l.split()))

    s = set()
    for i in l:
        if l.count(i) % 2 is not 0:
            s.add(i)
    s = map(str,sorted(list(s)))
    print("Case #" + str(T+1) + ": " + " ".join(s))




