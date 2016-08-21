inp = open("input.in", "r")
outp = open("output.out", "w")

check_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
             'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
             'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}


t = int(inp.readline().rstrip())

for x in range(t):
    s = inp.readline().rstrip()
    base = check_map[s[0]]
    r = s[0]

    i = 1
    while i < len(s):
        temp = r
        if check_map[s[i]] < base:
            r = temp + s[i]
        else:
            base = check_map[s[i]]
            r = s[i] + temp
        i += 1

    outp.write("Case #" + str(x+1) + ": " + r +"\n")


inp.close()
outp.close()