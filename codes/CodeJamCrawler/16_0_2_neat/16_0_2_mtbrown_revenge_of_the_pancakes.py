def main():
    cases = int(input())

    for case in range(1, cases + 1):
        num_flips = flips_required(input())
        print("Case #{0}: {1}".format(case, num_flips))


def flips_required(stack):
    last_orientation = '+'
    num_flips = 0

    for c in stack[::-1]:
        if c != last_orientation:
            last_orientation = c
            num_flips += 1

    return num_flips


if __name__ == "__main__":
    main()
