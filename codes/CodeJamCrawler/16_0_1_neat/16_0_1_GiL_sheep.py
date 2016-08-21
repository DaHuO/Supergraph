with open("A-large.in", "r") as fin, open("output.out", "w") as fout:
    T = int(fin.readline().strip())
    print(T)
    for i in range(T):
        keys = [0,1,2,3,4,5,6,7,8,9]
        seen = {key: False for key in keys}
        n = int(fin.readline().strip())
        v = n
        if n == 0:
            result = "INSOMNIA"
        else:
            result = 0
            n = str(n)
            while True:
                for digit in n:
                    digit = int(digit)
                    if not seen[digit]:
                        seen[digit] = True
                if False not in seen.values():
                    result = n
                    break
                else:
                    n = int(n)
                    n += v
                    n = str(n)
        fout.write("Case #{}: {}\n".format(i+1, result))

    print("done")
