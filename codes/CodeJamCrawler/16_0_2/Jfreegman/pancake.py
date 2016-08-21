import sys

def pancake(T):
    lines = open(T).read().split('\n')
    num = int(lines[0])

    for i in xrange(1, num+1):
        stack = lines[i]
        count = 0 if stack[-1] == '+' else 1
        length = len(stack)

        for j in xrange(length-1):
            if stack[j] != stack[j+1]:
                count += 1

        print "Case #" + str(i) + ": " + str(count)

if __name__ == '__main__':
    pancake(sys.argv[1])
