i_file = open('A-large.in', 'r')
o_file = open('output.txt', 'w')

T = int(i_file.readline())
for t in range(T):
    S = str(i_file.readline())
    temp = ""

    for l in S:
        if len(temp) == 0:
            temp = l
        elif ord(l) >= ord(temp[0]):
            temp = l + temp
        else:
            temp += l
    o_file.write("Case #" + str(t+1) + ": " + temp)

i_file.close()
o_file.close()
