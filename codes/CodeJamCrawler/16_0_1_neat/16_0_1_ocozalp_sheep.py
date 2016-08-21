def solve(n):
    visited = set()
    digits = set()
    number = n
    while True:
        if number in visited:
            return 'INSOMNIA'

        number2 = number
        while number2 > 0:
            digits.add(number2 % 10)
            number2 /= 10

        if len(digits) == 10:
            return str(number)

        visited.add(number)
        number += n

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n = int(raw_input())
        result = solve(n)
        print 'Case #%d: %s' % (i, result)

if __name__ == '__main__':
    main()
