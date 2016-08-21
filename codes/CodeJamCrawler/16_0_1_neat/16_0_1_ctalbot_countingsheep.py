import sys
import math

MAX_TESTCASES = 100
MAX_N = int(math.pow(10, 6))


def main():
    casefile = open(sys.argv[1], 'r')
    cases = int(casefile.readline())

    for i in range(1, cases+1):
        sleep_list = resetsleep()
        trysleep(i, int(casefile.readline()), sleep_list)


def trysleep(case, N, sleep_list):
    for i in range(1, MAX_N):
        newN = i*N
        listN = list(str(newN))
        for j in listN:
            sleep_list[int(j)] = True
            isasleep = checksleep(sleep_list)
            if isasleep:
                print "Case #" + str(case) + ": " + str(newN)
                return
    print "Case #" + str(case) + ": INSOMNIA"


def resetsleep():
    return [False for _ in range(0, 10)]


def checksleep(sleep_list):
    for sleep in sleep_list:
        if sleep is False:
            return False
    return True

main()
