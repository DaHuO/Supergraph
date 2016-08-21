i_file = open("input.txt", "r")
o_file = open("output.txt", "w")

def flip(s, i):
    flipped = ""
    to_flip = s[:i]
    for ch in to_flip[::-1]:
        if ch == "+":
            flipped += "-"
        else:
            flipped += "+"
    return flipped + s[i:]

cases = int(i_file.readline().strip())
for case in range(cases):
    s = i_file.readline().strip()
    flips = 0
    end = "+" * len(s)
    while s != end:
        if len(s) == 1 and s[0] == "-":
            flips += 1
            break
        if len(s) == 2 and s[0] == "+":
            flips += 2
            break
        if s[0] == "-":
            index = s.find("-+")
            if index == -1:
                flips += 1
                break
            s = flip(s, index + 1)
            flips += 1
            continue
        if s[0] == "+":
            s = flip(s, s.find("+-") + 1)
            flips += 1
            continue
    result = "Case #"+str(case+1)+": "+str(flips)+"\n"
    o_file.write(result)

i_file.close()
o_file.close()