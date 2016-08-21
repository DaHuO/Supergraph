import sys


def main():

    #f = open('A-small-attempt0.in', 'r')
    f = open('A-large.in', 'r')
    fout = open('a.out', 'w')

    case = int(f.readline())

    c = 1
    while c <= case:
        n = int(f.readline())

        if n == 0:
            fout.write('Case #%d: INSOMNIA\n' % c)
        else:
            big_num = [0]
            digit_set = set()

            while len(digit_set) < 10:
                big_num[0] += n

                i = 0
                carry = 0
                while i < len(big_num):
                    big_num[i] += carry
                    carry = big_num[i]/10
                    big_num[i] %= 10
                    i += 1

                while carry:
                    big_num.append(carry % 10)
                    carry /= 10

                digit_set |= set(big_num)

            fout.write('Case #%d: ' % c)
            i = len(big_num) - 1
            while i >= 0:
                fout.write(str(big_num[i]))
                i -= 1
            fout.write('\n')
        c += 1




if __name__ == '__main__':
    main()
