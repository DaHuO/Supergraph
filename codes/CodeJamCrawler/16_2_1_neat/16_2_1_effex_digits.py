problem_name = 'digits'
#ifilename = 'test.in'
#ifilename = 'A-small-attempt1.in'
ifilename = 'A-large.in'
ofilename = 'solution--' + problem_name + '--' + ifilename.split('.')[0] + '.txt'

ifile = open(ifilename, 'r')
num_cases = int(ifile.readline())

ofile = open(ofilename, 'w')

class Case:
    pass
    
def next_case(f):
    line = f.readline()
    if line == '':
        return []

    c = Case()
    c.s = line.strip()
    c.s = [c for c in c.s]
    return c

def find_ans_str(c):
    ans_str = ''

    c0 = c.s.count('Z')
    c2 = c.s.count('W')
    c4 = c.s.count('U')
    c6 = c.s.count('X')
    c8 = c.s.count('G')
    for x in range(c0):
        c.s.remove('E')
        c.s.remove('R')
        c.s.remove('O')
    for x in range(c2):
        c.s.remove('T')
        c.s.remove('O')
    for x in range(c4):
        c.s.remove('F')
        c.s.remove('O')
        c.s.remove('R')
    for x in range(c6):
        c.s.remove('S')
        c.s.remove('I')
    for x in range(c8):
        c.s.remove('E')
        c.s.remove('I')
        c.s.remove('H')
        c.s.remove('T')

    c1 = c.s.count('O')
    c3 = c.s.count('H')
    c5 = c.s.count('F')
    c7 = c.s.count('S')

    for x in range(c1):
        c.s.remove('N')
        c.s.remove('E')
    for x in range(c3):
        c.s.remove('T')
        c.s.remove('R')
        c.s.remove('E')
        c.s.remove('E')
    for x in range(c5):
        c.s.remove('I')
        c.s.remove('V')
        c.s.remove('E')
    for x in range(c7):
        c.s.remove('E')
        c.s.remove('V')
        c.s.remove('E')
        c.s.remove('N')

    c9 = c.s.count('I')

    ans_str += c0*'0'
    ans_str += c1*'1'
    ans_str += c2*'2'
    ans_str += c3*'3'
    ans_str += c4*'4'
    ans_str += c5*'5'
    ans_str += c6*'6'
    ans_str += c7*'7'
    ans_str += c8*'8'
    ans_str += c9*'9'
    
    return ans_str

c = next_case(ifile)
casenum = 1
while c != []:

    ans_str = 'Case #' + str(casenum) + ': '
    ans_str += find_ans_str(c)
#    print(ans_str)
    ofile.write(ans_str + '\n')
    c = next_case(ifile)
    casenum += 1

if casenum - 1 != num_cases:
    print('error: not all cases read')
ifile.close()
ofile.close()
