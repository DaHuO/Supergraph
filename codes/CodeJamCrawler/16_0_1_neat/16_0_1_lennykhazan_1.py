T = int(input())

for t in range(T):
    N = int(input())

    done = False
    digits = set()
    for c in range(1, 1000000):
        for char in str(N*c):
            digits.add(char)

        if len(digits) == 10:
            print('Case #' + str(t+1) + ': ' + str(c*N))
            done = True
            break

    if not done:
        print ('Case #' + str(t+1) + ': ' + 'INSOMNIA')
