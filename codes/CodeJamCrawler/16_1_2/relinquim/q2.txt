i_file = open('B-large.in', 'r')
o_file = open('output.txt', 'w')

T = int(i_file.readline())
for t in range(T):
    N = int(i_file.readline())
    occ = {}
    for n in range(2*N-1):
        temp = [int(x) for x in i_file.readline().split()]
        for i in temp:
            if i in occ.keys():
                occ[i] += 1
            else:
                occ[i] = 1
    answer = ""
    for j in sorted(occ.keys()):
        if occ[j] % 2:
            answer += " " + str(j)
    o_file.write("Case #" + str(t+1) + ":" + answer + "\n")

i_file.close()
o_file.close()