f = open('A-large.in', 'r')
fout = open('A-small-output.txt', 'w')
T = int(f.readline())

for i in range(1, T+1):
    sleep = []
    N = int(f.readline())
    addition = N
    while sleep != ['0','1','2','3','4','5','6','7','8','9']:
        if N == 0:
            N = 'INSOMNIA'
            break
        else:
            for a in str(N):
                if a not in sleep:
                    sleep.append(a)
            sleep.sort()
            if sleep == ['0','1','2','3','4','5','6','7','8','9']:
                break
            N = N + addition
    fout.write('Case #' + str(i) + ':' + ' ' + str(N) + '\n')

f.close()
fout.close()
