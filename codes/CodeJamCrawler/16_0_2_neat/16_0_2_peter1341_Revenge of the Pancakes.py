import sys

T = input()
with open('output.txt', 'w') as f:
    for case in range(T):
        f.write("Case #" + str(case + 1) + ": ")
        S = sys.stdin.readline()
        S=S.replace("\n", "")
        i = 0
        cnt = 0
        print S.__repr__()
        while i < S.__len__():
            while i + 1 < S.__len__() and S[i] == S[i + 1]:
                i += 1
            if i + 1 < S.__len__() and S[i] != S[i + 1]:
                cnt += 1
            i += 1
        if S[S.__len__() - 1] == '-':
            cnt += 1
        f.write(str(cnt) + "\n")
