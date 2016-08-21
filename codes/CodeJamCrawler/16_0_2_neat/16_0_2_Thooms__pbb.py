

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        s = input()
        k = 0
        i = 0
        plus, minus = False, False

        if s[i] == '-': # treat the first -'s separately
            k += 1
            while i < len(s) and s[i] == '-':
                i += 1

        # then each '+-' pattern (repetitions don't count) augment k by 2
        while i < len(s) - 1:
            plus, minus = False, False
            # search for +'s
            while i < len(s) and s[i] == '+':
                plus = True
                i += 1
            # search for -'s, if there's none at the end of the string, the +'s count for nothing
            while i < len(s) and s[i] == '-':
                minus = True
                i += 1

            if plus and minus:
                k += 2


        print('Case #{}: {}'.format(t+1, k))
