import sys

fd = open(sys.argv[1], 'r')

ncases = int(fd.readline()[:-1])

for case in range(1, ncases+1):
    npart = int(fd.readline()[:-1])
    sens = list(map(int, fd.readline()[:-1].split()))

    print("Case #" + str(case) + ":", end=' ')
    while any(sens):

        done = False

        maj = max(sens)
        maj1 = sens.index(maj)
        print(chr(maj1+65), end='')

        sens[maj1] -= 1

        maj = max(sens)
        maj2 = sens.index(maj)

        senscpy = sens[:]
        senscpy[maj2] -= 1
        absmaj = abs(sum(senscpy))//2
#        print(absmaj)
        if not list(filter(lambda x: x > absmaj, senscpy)):
            print(chr(maj2+65), end='')
            sens[maj2] -= 1

            print(' ', end='')
            continue

        print(' ', end='')

    print()
