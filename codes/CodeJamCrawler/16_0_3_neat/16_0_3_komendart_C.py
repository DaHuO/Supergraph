def main(fout):
    N = 32
    J = 500
    
    print("Case #1:", file=fout)
    for i in range(1 << (N - 1), 1 << N):
        s = bin(i)[2:]
        if len(s) != N or s[0] != '1' or s[-1] != '1': continue
        a = []
        for j in range(2, 11):
            t = int(s, j)
            for k in range(2, 20):
                if t % k == 0:
                    a.append(k)
                    break
        if len(a) == 9:
            print(s, *a, file=fout)
            J -= 1
            if J == 0: break
        

with open("output.txt", 'w') as fout:   
    main(fout)