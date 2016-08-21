
def flip_count(s):
    def flip(s):
        if n == '-':
            return '+'
        else:
            return '-'

    def num_flip(s, num = 0):
        same = True
        side = s[0]
        for i in s:
            if not(i == side):
                same = False

        if not(same):
            if s == '-':
                return ('+', 1+num)
            else:
                index = 0
                sign = s[index]
                new_s = ''
                while index != len(s)-1 and sign == s[index + 1] :
                    index += 1
                if sign == '-':
                    s = '+'*(index+1) + s[index+1:]
                    return num_flip(s, num + 1)
                else:
                    s = s[index + 1:]
                    return num_flip(s, num + 1)

        elif same and side == '+':
            return ('+', 0+num)
        else:
            return ('+', 1+num)

    return num_flip(s)[1]

if __name__ == '__main__':
    file = open('B-large.in.txt', 'r')
    line = 1
    case_number = 0
    for i in file:
        if line != 1:
            print('Case #' + str(case_number) + ': ' + str(flip_count((i.strip()))))
        else:
            line += 1
        case_number += 1