import string

ALPHA = string.ascii_uppercase


def find_max(T):
    max_key, max_value = None, None
    for key, value in T.iteritems():
        if max_value is None or value > max_value:
            max_key, max_value = key, value
    return max_key, max_value


def solve(T):
    T = {ALPHA[idx]: int(N) for idx, N in enumerate(T.split())}
    output = ""

    while any(T.values()):
        key1, value1 = find_max(T)
        if value1 > 0:
            T[key1] -= 1
            output += key1

        key2, value2 = find_max(T)
        T_copy = dict(**T)
        T_copy[key2] -= 1
        key3, value3 = find_max(T_copy)

        if value2 > 0 and (not value3 or value3 <= (sum(T_copy.values())) / 2):
            T[key2] -= 1
            output += key2

        output += ' '

    return output


def main():
    T = input()
    for N in xrange(T):
        raw_input()
        print "Case #{}: {}".format(N + 1, solve(raw_input()))

if __name__ == "__main__":
    main()
