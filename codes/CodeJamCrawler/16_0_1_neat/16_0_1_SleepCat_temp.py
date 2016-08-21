import numpy as np
size = int(raw_input())

for i in range(size):
    N = int(raw_input())
    if N == 0:
        print 'Case #' + str(i + 1) + ': INSOMNIA'
    else:
        checklist = np.zeros(10, np.bool_)
        j = 0
        while False in checklist:
            j += 1
            numberlist = map(int, str(N*j))
            for number in numberlist:
                checklist[number] = True
        print 'Case #' + str(i + 1) + ': ' + str(N*j)