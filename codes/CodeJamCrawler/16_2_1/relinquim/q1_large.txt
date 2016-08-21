i_file = open('A-large.in', 'r')
o_file = open('output.txt', 'w')

T = int(i_file.readline())
for t in range(T):
    S = str(i_file.readline())
    temp = []
    temp.append(S.count("Z"))
    temp.append(S.count("O") - S.count("W") - S.count("U") - S.count("Z"))
    temp.append(S.count("W"))
    temp.append(S.count("H") - S.count("G"))
    temp.append(S.count("U"))
    temp.append(S.count("F") - temp[4])
    temp.append(S.count("X"))
    temp.append(S.count("S") - temp[6])
    temp.append(S.count("G"))
    temp.append(S.count("I") - temp[5] - temp[6] - temp[8])
    ans = ""

    for i in range(len(temp)):
        ans += temp[i] * str(i)

    o_file.write("Case #" + str(t+1) + ": " + ans + "\n")

i_file.close()
o_file.close()
