import sys

def count_sheep(n):
    digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 1
    while digit_list != []:
        if i > 10000:
            return "INSOMNIA"
        res = n * i
        c = res
        # print c
        while c != 0:
            rem = c % 10
            # print rem
            if rem in digit_list:
                digit_list.remove(rem)
                # print digit_list
                if digit_list == []:
                    return res
            c = c / 10
        i = i + 1

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        print "Case #%d:" % (i + 1),
        print count_sheep(N)


