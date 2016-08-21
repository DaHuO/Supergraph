def sunnySideUp(pattern):
    if len(set(pattern)) == 1:
        if pattern[0] == '+':
            return True
    return False


def flip(pattern, end):
    pattern = list(pattern)

    flipper = '+'
    if pattern[0] == '+':
        flipper = '-'

    for i in range(end):
        pattern[i] = flipper

    return ''.join(pattern)


def getFlips(pattern):
    flips = 0

    if len(pattern) == 1:
        if pattern == '-':
            return flips + 1

    while not sunnySideUp(pattern):
        i = 1
        while i < len(pattern) and pattern[i] == pattern[0]:
            i += 1
        pattern = flip(pattern, i)
        flips += 1

    return flips


def main():
    cases = int(raw_input())
    for i in range(cases):
        result = getFlips(raw_input())
        print "Case #" + str(i + 1) + ": " + str(result)
    return

if __name__ == "__main__":
    main()
