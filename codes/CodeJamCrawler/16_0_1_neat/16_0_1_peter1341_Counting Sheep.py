T = input()
with open('output.txt', 'w') as f:
    for case in range(T):
        f.write("Case #" + str(case+1) + ": ")
        N = input()
        if N == 0:
            f.write("INSOMNIA\n")
            continue
        test = [False] * 10
        tester = N
        cnt = 0
        while cnt < 10:
            tmp = tester
            while tmp > 0:
                if not test[tmp % 10]:
                    test[tmp % 10] = True
                    cnt += 1
                tmp /= 10
            tester += N
        tester-=N
        f.write(str(tester)+"\n")

# 5
# 0
# 1
# 2
# 11
# 1692