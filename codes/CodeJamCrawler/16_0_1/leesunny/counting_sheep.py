def main():
    i = 0
    while True:
        try:
            t = int(input())
            if i != 0:  # Skip first line
                # print(t)
                print("Case #{}: {}".format(i, count_sheep(t)))
        except EOFError:
            break
        i += 1


def count_sheep(n):
    if n == 0:
        return "INSOMNIA"
    else:
        digits_seen = set()
        x = 0
        while len(digits_seen) < 10 :
            x = n if x == 0 else x + n
            digits_seen.update(list(str(x)))
        return x


if __name__ == "__main__":
    main()
