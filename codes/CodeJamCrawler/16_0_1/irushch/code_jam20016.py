numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def counting_sheeps(n, i=1):
    if n == 0:
        return 'INSOMNIA'

    number = n * i
    for item in str(number):
        if item in numbers:
            numbers.remove(item)

    if numbers:
        return counting_sheeps(n, i+1)
    else:
        return number


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        # read a list of integers
        n = raw_input()
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        print "Case #{}: {}".format(i, counting_sheeps(int(n)))
