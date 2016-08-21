t = input()
for poo in range(t):
    n = input()
    ans = ""
    if n == 0:
        ans = "INSOMNIA"
    else:
        hack = set()
        for i in range(1, 100):
            a = i * n
            for j in str(a):
                hack.add(j)
            if len(hack) == 10:
                ans = str(i * n)
                break 
        else:
            ans = "INSOMNIA"

    print "Case #" + str(poo + 1) + ": " + ans
