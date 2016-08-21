def main():
    cases = int(input())

    for case in range(cases):
        digits_seen = set()
        n = int(input())

        if n == 0:
            print("Case #{0}: INSOMNIA".format(case + 1))
            continue

        i = 0
        cur_n = n
        while True:
            digits_seen.update(str(cur_n))
            if len(digits_seen) >= 10:
                break

            cur_n += n
            i += 1

        print("Case #{0}: {1}".format(case + 1, cur_n))


if __name__ == "__main__":
    main()
