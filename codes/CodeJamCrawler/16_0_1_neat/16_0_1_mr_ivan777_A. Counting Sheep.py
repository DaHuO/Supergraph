__author__ = 'ivan_pavlov'

with open("in.txt", "r") as f:
    size = next(f)
    out = open("res.txt", "w")
    for index, N in enumerate(list(map(int, f.readlines()))):
        print(N)
        out.write("Case #"+str(index+1)+": ")
        digit_set = set()
        ok = False
        for i in range(1, 10000000):
            cur_n = i * N
            digit_set.update(set(str(cur_n)))
            if len(digit_set) == 10:
                out.write(str(cur_n) + "\n")
                ok = True
                break
        if not ok:
            out.write("INSOMNIA\n")


