# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def check_nb(number, i):
    if i == 0:
        if 'Z' in number:
            number.remove('Z')
            number.remove('E')
            number.remove('R')
            number.remove('O')
            return number, '0'
        else:
            return False, 0
    if i == 1:
        if 'X' in number:
            number.remove('S')
            number.remove('I')
            number.remove('X')
            return number, '6'
        else:
            return False, 0
    if i == 2:
        if 'W' in number:
            number.remove('T')
            number.remove('W')
            number.remove('O')
            return number, '2'
        else:
            return False, 0
    if i == 3:
        if 'U' in number:
            number.remove('F')
            number.remove('O')
            number.remove('U')
            number.remove('R')
            return number, '4'
        else:
            return False, 0
    if i == 4:
        if 'F' in number:
            number.remove('F')
            number.remove('I')
            number.remove('V')
            number.remove('E')
            return number, '5'
        else:
            return False, 0
    if i == 5:
        if 'S' in number:
            number.remove('S')
            number.remove('E')
            number.remove('V')
            number.remove('E')
            number.remove('N')
            return number, '7'
        else:
            return False, 0
    if i == 6:
        if 'G' in number:
            number.remove('E')
            number.remove('I')
            number.remove('G')
            number.remove('H')
            number.remove('T')
            return number, '8'
        else:
            return False, 0
    if i == 7:
        if 'H' in number:
            number.remove('T')
            number.remove('H')
            number.remove('R')
            number.remove('E')
            number.remove('E')
            return number, '3'
        else:
            return False, 0
    if i == 8:
        if 'O' in number:
            number.remove('O')
            number.remove('N')
            number.remove('E')
            return number, '1'
        else:
            return False, 0
    if i == 9:
        if 'N' in number:
            number.remove('N')
            number.remove('I')
            number.remove('N')
            number.remove('E')
            return number, '9'
        else:
            return False, 0


t = int(raw_input())
for case in xrange(1, t+1):
    number = list(raw_input())  # read a line with a single integer
    digits = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
    answer = ''
    for i in xrange(0,10):
        curr_number = True
        while curr_number:
            curr_number, new = check_nb(number, i)
            if curr_number != False:
                number = curr_number
                answer += new
    answer = ''.join(sorted(answer))
    print "Case #{}: {}".format(case, answer)
