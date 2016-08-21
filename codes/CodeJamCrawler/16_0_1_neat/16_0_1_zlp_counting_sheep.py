
with open('test.txt', 'r') as f_in:
    T = int(f_in.readline().strip())
    output = ""
    for i in range(T):
        res = [False] * 10
        N = int(f_in.readline())
        if N == 0:
            output += "Case #{}: INSOMNIA\n".format(i + 1)
            continue
        num = 0
        while not all(res):
            num += N
            for d in str(num):
                res[int(d)] = True
        output += "Case #{}: {}\n".format(i + 1, num)
    f_out = file('output.txt', 'w')
    f_out.write(output)
    f_out.close()
