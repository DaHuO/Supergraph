__author__ = 'texom512'

with open('A-large.in', 'r') as input_file:
    def input():
        return input_file.readline().strip()


    nb_cases = int(input())
    for case in range(1, nb_cases + 1):
        s = input()

        r = s[0]
        for c in s[1:]:
            if ord(c) >= ord(r[0]):
                r = c + r
            else:
                r += c

        print('Case #{}: {}'.format(case, r))