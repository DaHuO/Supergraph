import sys


def write_output(case, result):
    with open('output', 'a') as outp:
        towrite = "Case #%i: %s\n" % (case, str(result))
        outp.write(towrite)


def checker(seen, numbers):
    for char in numbers:
        if char not in seen:
            return False
        else:
            pass
    return True


def main():
    with open(sys.argv[1]) as f:
        contents = f.readlines()

    N = map(int, contents[1:])
    T = int(contents[0])

    numbers = '1234567890'

    case = 0

    for n in N:
        current = n
        seen = ''
        case += 1
        if n == 0:
            write_output(case, 'INSOMNIA')
        else:
            i = 0
            while True:
                i += 1
                seen = seen + str(current)
                if checker(seen, numbers):
                    write_output(case, current)
                    break
                else:
                    current = n * i


if __name__ == '__main__':
    main()
