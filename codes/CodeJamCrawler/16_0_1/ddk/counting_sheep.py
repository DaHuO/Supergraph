def solve(number):
    if number == 0:
        return 'INSOMNIA'
    else:
        digits = set('0123456789')
        answer = number
        digits = digits - set(str(answer))
        while len(digits) > 0:
            answer += number
            digits -= set(str(answer))
        return str(answer)


def run_program():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        number = int(raw_input())
        print "Case #{0}: {1}".format(i, solve(number))


if __name__ == '__main__':
    run_program()

