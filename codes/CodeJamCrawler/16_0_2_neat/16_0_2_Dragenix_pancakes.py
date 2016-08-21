f = open('B-large.in', 'r')
fout = open('B-output.txt', 'w')
T = int(f.readline())

for i in range(1, T+1):
    S = f.readline()
    count = 0
    for a in range(len(S)):
        if a == 0:
            if S[a] == '-':
                count += 1
        else:
            if (S[a]=='-') and (S[a-1]=='+'):
                count += 2
    fout.write('Case #' + str(i) + ':' + ' ' + str(count) + '\n')

f.close()
fout.close()