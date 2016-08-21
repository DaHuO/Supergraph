i_file = open('D-small-attempt0.in', 'r')
o_file = open('output.txt', 'w')

T = int(i_file.readline())
for t in range(T):
    K, C, S = [int(x) for x in i_file.readline().split(" ")]

    if K == S:
        answer = ""
        for i in range(K):
            answer += " " + str(i+1)
        o_file.write("Case #" + str(t+1) + ":" + answer + "\n")
    else:
        if S < (int(K/C) + (K%C>0)):
            o_file.write("Case #" + str(t+1) + ": IMPOSSIBLE\n")
        else:
            answer = ""
            for i in range(int(K/C)):
                temp = 1
                for j in range(C):
                    temp += (i*C) * (K**j) + (j) * (K**j)
                answer += " " + str(temp)
            if int(K%C) != 0:
                temp = max(int(K/C) * C * (K**(C-1)), 1)
                for j in range(K%C):
                    temp += (j) * (K**j)
                answer += " " + str(temp)
            o_file.write("Case #" + str(t+1) + ":" + answer + "\n")

i_file.close()
o_file.close()
