T = int(input())

for i in range(T):
    N = int(input())
    if N > 0:
        unseen_digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        k = 1
        while len(unseen_digits) > 0:
            last_count = k*N
            count = last_count
            while count > 0:
                last_digit = count % 10
                if last_digit in unseen_digits:
                    unseen_digits.remove(last_digit)
                count = count // 10
            k += 1
    else:
        last_count = "INSOMNIA"

    print ("Case #{0}: {1}".format(i+1, last_count))
