__author__ = 'valentinarho'


def check_new_digits(number, alreadycounted):
    count = 0
    for n in list(str(number)):
        n = int(n)
        if alreadycounted[int(n)] == False:
            count += 1
            alreadycounted[n] = True
    return count;


if __name__ == '__main__':

    nomefile = "A-large"

    # open file input
    input = open(nomefile + '.in', 'r')
    out = open(nomefile + '.out', 'w')

    # number of test case
    T = int(input.readline())

    for i in range(1, T + 1):  # da 1 a t
        N = int(input.readline())
        if N == 0:
            result = "INSOMNIA"
        else:
            count = 0
            digits = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False,
                      9: False}
            tmp = N
            count += check_new_digits(tmp, digits)
            while count != 10:
                tmp = tmp + N
                count += check_new_digits(tmp, digits)
            result = tmp

        out.write("Case #" + str(i) + ": " + str(result) + "\n")

    out.close()
    input.close()



