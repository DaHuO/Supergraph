with open('google.txt', 'r') as f:
    read_data = f.readlines()
    data = []
    for d in read_data:
        data.append(int(d))
    data = data[1:]
    line = 1
    for N in data:
        inc = 1
        seen_digits = set()
        insomnia_flag = False
        while 1:
            for char in str(N * inc):
                seen_digits.add(char)
            if inc > 1000:
                insomnia_flag = True
                break
            elif len(seen_digits) == 10:
                break
            inc += 1

        with open('google2.txt', 'a') as f2:
            if insomnia_flag:
                f2.write("Case #" + str(line) + ": INSOMNIA\n")
            else:
                f2.write("Case #" + str(line) + ": " + str(N * inc) + "\n")
        line += 1
