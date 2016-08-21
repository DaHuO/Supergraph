t = int(input())
for case in range(1,t+1):
    m = n = int(input())
    count = {i:False for i in range(10)}
    if m:
        while not all(count[i] for i in count):
            for c in list(str(m)):
                count[int(c)] = True
            m += n
        ans = m - n
    else:
        ans = "INSOMNIA"
    print ("Case #{}: {}".format(case, ans))
