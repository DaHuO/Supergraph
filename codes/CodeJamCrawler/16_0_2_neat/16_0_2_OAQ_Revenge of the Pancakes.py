f = open('B-large.in', 'r')
output = open('B-large.txt', 'w')

pancake = []
number = int(f.readline())

i = 0
while number > i:
    i += 1
    pancake.append(f.readline().strip('\n'))

case = 0
for pancake in pancake:
    case += 1
    N = 0
    side = []
    for digit in pancake:
        side.append(digit)

    while side.count('+') <= len(side):
        if side.count('+') == len(side):
            output.writelines('Case #%i: %d\n' % (case, N))
            break
        if side[0] == '+':
            first = side.index('-')
            for i in xrange(first):
                if side[i] == '+':side[i] = '-'
                else:side[i] = '+'
            side[:first] = side[first-1::-1]
            N += 1

        last = side[-1::-1].index('-')
        if last != 0:
            for i in xrange(len(side[:-last])):
                if side[i] == '+':side[i] = '-'
                else:side[i] = '+'
            side[:-last] = side[-last-1::-1]
            N += 1
        else:
            for i in xrange(len(side)):
                if side[i] == '+':side[i] = '-'
                else:side[i] = '+'
            side.reverse()
            N += 1

