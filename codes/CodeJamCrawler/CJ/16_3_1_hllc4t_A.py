
A = 65


def sort_tuples(arr):
    return sorted(arr, key=lambda tup: tup[0], reverse=True)


def getsum(part):
    sum = 0
    for i in part:
        sum += i[0]
    return sum


def check_all(part, ii, summ):
    for i in xrange(0, len(part)):
        if i == ii:
            if (part[i][0] - 1) * 2 > summ:
                break
        else:
            if part[i][0] * 2 > summ:
                return False

    return True


def check_two(part, i1, i2, summ):
    for i in xrange(0, len(part)):
        if i == i1 or i == i2:
            if (part[i][0] - 1) * 2 > summ:
                break
        else:
            if part[i][0] * 2 > summ:
                return False
    return True


def perform_step(part, summ):
    constraint = 2
    taken = 0
    i = 0
    result = ""
    for i in xrange(0, len(part)):
        if (part[i][0] > 0) and check_all(part, i, summ - 1):
            result += part[i][1]
            summ -= 1
            part[i] = (part[i][0] - 1, part[i][1])
            taken += 1
            if taken == constraint:
                break

    if summ > 0 and taken == 0:
        for i1 in xrange(0, len(part)):
            if (part[i1][0] > 0):
                for i2 in xrange(i1 + 1, len(part)):
                    if (part[i1][0] > 0):
                        if check_two(part, i1, i2, summ - 2):
                            result += part[i1][1]
                            result += part[i2][1]
                            summ -= 2
                            part[i1] = (part[i1][0] - 1, part[i1][1])
                            part[i2] = (part[i2][0] - 1, part[i2][1])
                            return result, part, summ


    return result, part, summ


t = int(raw_input())

for tt in xrange(1, t + 1):
    n = int(raw_input())
    p = raw_input().split(" ")
    part = list()
    answer = ""

    for nn in xrange(0, n):
        part.append((int(p[nn]), chr(A + nn)))

    summ = getsum(part)
    part = sort_tuples(part)

    while summ > 0:
        chunk, part, summ = perform_step(part, summ)

        answer += chunk
        if summ > 0:
            answer += " "

    print "Case #" + str(tt) + ": " + str(answer)
