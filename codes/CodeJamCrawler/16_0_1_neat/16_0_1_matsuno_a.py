import sys

def increment(myself, addend):
    # assert(i >= j)
    i = len(myself) - 1
    j = len(addend) - 1
    carry = 0
    while i >= 0:
        if j < 0:
            if carry == 0:
                break
            myself[i] += carry
            if myself[i] >= 10:
                carry = 1
                myself[i] -= 10
            else:
                carry = 0
            i -= 1
            continue

        myself[i] += addend[j] + carry
        if myself[i] >= 10:
            carry = 1
            myself[i] -= 10
        else:
            carry = 0
        i -= 1
        j -= 1

    if carry > 0:
        myself.insert(0, carry)

def do(digits):
    if len(digits) == 1 and digits[0] == 0:
        return 'INSOMNIA'

    s = [0] * len(digits)
    digit_set = 0
    while True:
        increment(s, digits)
        for d in s:
            digit_set |= 1 << d
        if digit_set == 1023:
            break

    return ''.join([chr(ord('0') + d) for d in s])

def main():
    t = int(sys.stdin.readline())
    for i in xrange(t):
        print "Case #{0}: {1}".format(i + 1, do([ord(c) - ord('0') for c in list(sys.stdin.readline().strip())]))

if __name__ == '__main__':
    main()
