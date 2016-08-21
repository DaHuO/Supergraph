i_file = open('A-large.in', 'r')
o_file = open('output.txt', 'w')

T = int(i_file.readline())
for t in xrange(1, T+1):
    N = int(i_file.readline())
    P = [int(x) for x in i_file.readline().split(" ")]

    max_i = chr(65)
    max_s = 0
    ans = ""

    while max(P) != 0:
        max_s = max(P)
        max_i = [i for i, x in enumerate(P) if x == max_s]
        tot = sum(P)

        if max_s == (tot/2)+2:
            temp = chr(max_i[0]+65) + chr(max_i[0]+65)
            P[max_i[0]] -= 2

        elif max_s == (tot/2)+1:
            temp = chr(max_i[0]+65)
            P[max_i[0]] -= 1

        else:
            if len(max_i) > 1 and len(max_i) != 3:
                temp = chr(max_i[0]+65) + chr(max_i[1]+65)
                P[max_i[0]] -= 1
                P[max_i[1]] -= 1
            else:
                temp = chr(max_i[0]+65)
                P[max_i[0]] -= 1
        ans += temp + " "

    o_file.write("Case #" + str(t) + ": " + ans[:-1] + "\n")

i_file.close()
o_file.close()
