__author__ = 'valentinarho'


def swap(pancake):
    res = pancake.rfind('-');
    if res == -1:
        return 0, pancake
    else:
        if pancake[0] == '+':
            # reverse the biggest group of ones
            j = 0
            tmp_pancake = ''
            while pancake[j] == '+':
                tmp_pancake += '-'
                j+=1
            pancake = tmp_pancake + pancake[len(tmp_pancake):]
            return 1, pancake
        else:
            reversed = list(pancake[0:res+1][::-1])
            for i in range(0, res+1):
                if reversed[i] == '+':
                    reversed[i] = '-'
                else:
                    reversed[i] = '+'

            return 1, ''.join(map(str, reversed)) + pancake[res+1:]

if __name__ == '__main__':

    nomefile = "B-large"

    # open file input
    input = open(nomefile + '.in', 'r')
    out = open(nomefile + '.out', 'w')

    # number of test case
    T = int(input.readline())

    for i in range(1, T + 1):  # da 1 a t
        pancake = input.readline()
        res = 1
        count = 0
        while res != 0:
            res,pancake = swap(pancake);
            count += res

        out.write("Case #" + str(i) + ": " + str(count) + "\n")

    out.close()
    input.close()



