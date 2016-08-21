input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

tokens = input.readline().split(' ')

T = int(tokens[0])

for X in range(1,T+1):
    N = int(input.readline().strip())
    if N == 0:
        print "Case #" + str(X) +": INSOMNIA"
        output.write("Case #" + str(X) + ": INSOMNIA\n")
        continue

    observed = [False] * 10
    i = 1

    while sum(observed) < 10:
        for n in str(i*N):
            observed[int(n)] = True
        i += 1
    print "Case #" + str(X) + ": " + str((i-1)*N)
    output.write("Case #" + str(X) + ": " + str((i-1)*N) + "\n")
