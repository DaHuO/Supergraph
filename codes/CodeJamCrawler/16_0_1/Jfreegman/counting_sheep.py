import sys

def countSheep(T):
    lines = open(T).read().split('\n')
    num = int(lines[0])

    for i in xrange(1, num+1):
        explored = set()
        N = int(lines[i])
        if N == 0:
            print "Case #" + str(i) + ": INSOMNIA"
            continue

        j = 0
        while True:
            j += 1
            number = N * j
            for ch in str(number):
                explored.add(ch)

            if (len(explored) == 10):
                found = True
                print "Case #" + str(i) + ": " + str(number)
                break

if __name__ == '__main__':
    countSheep(sys.argv[1])
