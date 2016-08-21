ip = open('B-large.in', 'r')
op = open('output.txt', 'w')

num_cases = int(ip.readline())

for x in range(num_cases):
    S = ip.readline().rstrip('\n')
    num_flips = 0
    for i in range(len(S)):
        if i == 0:
            if S[i] == '-':
                num_flips += 1
            else:
                pass
        else:
            if (S[i]=='-') and (S[i-1]=='+'):
                num_flips += 2
            else:
                pass
    op.write('Case #' + str(x+1) + ': ' + str(num_flips) + '\n')

ip.close()
op.close()
