import fileinput


def count_sheep(N):
    def digits_generator():
        i = 1;
        history = list()
        digits_in_ixN = list(str(i*N))
        while digits_in_ixN not in history:
            history.append(digits_in_ixN)
            yield (i*N, digits_in_ixN)
            i+=1
            digits_in_ixN = list(str(i*N))

    seen_digits = set()
    dg = digits_generator()
    for ixN, digits in dg:
        seen_digits = seen_digits.union(set(digits))
        if seen_digits == {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
            return str(ixN)
    return "INSOMNIA"


def main():
    lines = [line.strip() for line in fileinput.input()][1:]

    for case, N in enumerate(lines, 1):
        last_number = count_sheep(int(N))
        print "Case #{case}: {last_number}".format(case=case, last_number=last_number)


if __name__ == '__main__':
    main()
