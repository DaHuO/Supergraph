import sys

def get_sleep_number(N):
    seen_digits = [0 for i in range(0, 10)]
    last_number = N

    def all_done():
        for i in range(0, 10):
            if (seen_digits[i] == 1):
                continue
            return False
        return True

    def update_seen_digits(N):
        digit_list = [int(i) for i in str(N)]
        for i in range(len(digit_list)):
            v = digit_list[i]
            seen_digits[v] = 1
        return

    iter = 1
    while all_done() == False:
        last_number = iter * N
        iter += 1
        update_seen_digits(last_number)

    return last_number

def main():
    num_tests = int(sys.stdin.readline())
    for tc in xrange(1, num_tests+1):
        N = int(sys.stdin.readline())

        if N == 0:
            sleep_number = "INSOMNIA"
        else:
            sleep_number = str(get_sleep_number(N))

        print "Case #" + str(tc) + ": " + sleep_number

    return


# start it all
if __name__ == "__main__":
    main()
