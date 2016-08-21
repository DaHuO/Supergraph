import sys
import math
sys.setrecursionlimit(100000)


for _test in range(1, int(raw_input()) + 1):
    answer = []

    N = int(raw_input())

    data = map(int, raw_input().split())

    T = sum(data)

    data = [[data[i], chr(65+i)] for i in range(N)]

    data += [[0, '$']]

    while T > 0:
        data.sort(reverse=True)
        #print data

        x = 0

        if data[0][0] == data[1][0]:
            if data[2][0] + 1 <= data[0][0]:
                x = 2
                answer.append(data[0][1] + data[1][1])
                data[0][0] -= 1
                data[1][0] -= 1
            else:
                x = 1
                answer.append(data[0][1])
                data[0][0] -= 1
        elif data[1][0] == data[2][0]:
            x = min(2, data[0][0])

            answer.append(x * data[0][1])
            data[0][0] -= x
        else:
            x = min(2, data[0][0] - data[1][0])
            answer.append(x * data[0][1])
            data[0][0] -= x

        T -= x

    print "Case #{}: {}".format(_test, ' '.join(answer))
"""
import sys
import math
sys.setrecursionlimit(100000)


for _test in range(1, int(raw_input()) + 1):
    answer = []

    N = int(raw_input())

    data = map(int, raw_input().split())

    T = sum(data)

    data = [(data[i], chr(65+i)) for i in range(N)]


    while T > 0:
        data.sort(reverse=True)
        print data

        it_done = False

        for i in range(N):
            found = False
            for j in range(N):
                if j != i:
                    if data[j][0] > (T-2) / 2:
                        found = True
                        break

            if not found:
                data[i][0] -= 2
                answer.append(2 * data[i][1])
                it_done = True
                break

        if not it_done:
            for i in range(N):
                found = False
                for j in range(N):
                    if j != i:
                        if data[j][0] > (T-1) / 2:
                            data[i][0] -= 1
                            found = True
                            break

            if not found:
                answer.append(2 * data[i][1])
                break

        if found:
            for i in range(N):
                for j in range(N):


    print "Case #{}: {}".format(_test, ' '.join(answer))

"""