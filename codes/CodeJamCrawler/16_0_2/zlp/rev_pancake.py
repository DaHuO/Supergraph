
with open("test.txt", 'r') as f_in:
    T = int(f_in.readline().strip())
    output = ""
    for i in range(1, T + 1):
        s = f_in.readline().strip()
        s += '+'
        res = 0
        for k in range(len(s) - 1):
            if s[k] != s[k + 1]:
                res += 1
        output += "Case #{}: {}\n".format(i, res)

    f_out = open("output.txt", 'w')
    f_out.write(output)
    f_out.close()
