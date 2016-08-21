i_file = open('B-large.in', 'r')
o_file = open('output.txt', 'w')

T = int(i_file.readline())
for t in range(T):
    S = str(i_file.readline())
    flips = 0
    N = len(S)
    while S.find("-") > -1:
        i = S.find("+")
        if i == -1:
            i = N - 1
        if i == 0:
            j = S.rfind("-")
            temp = ""
            for k in range(j+1):
                if S[k] == "+":
                    temp += "-"
                else:
                    temp += "+"
            temp += S[j+1:N]
            S = temp
            flips += 1
        else:
            temp = ""
            for k in range(i):
                if S[k] == "+":
                    temp += "-"
                else:
                    temp += "+"
            temp += S[i:N]
            S = temp
            flips += 1
    o_file.write("Case #" + str(t+1) + ": " + str(flips) + "\n")

i_file.close()
o_file.close()
