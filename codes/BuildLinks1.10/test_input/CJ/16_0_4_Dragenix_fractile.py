f = open('D-small-attempt0.in', 'r')
fout = open('D-OUTPUT', 'w')
T = int(f.readline())
for i in range(1,T+1):
    line = f.readline().split(' ')
    S = int(line[2])
    fout.write('Case #'+str(i)+':'+' ')
    for i in range(1,S+1):
        fout.write(str(i))
        fout.write(' ')
    fout.write('\n')
