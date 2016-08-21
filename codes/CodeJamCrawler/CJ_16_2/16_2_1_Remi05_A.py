import sys
import math
import string
import itertools

def formatOutput(n, result):
    return 'Case #' +  str(n) + ': ' + result + '\n'


def solveProblem(file):
    line = file.readline().strip()
    number = [0] * 10

    z_count = line.count('Z')
    if z_count > 0:
        line = line.replace('Z', '', z_count).replace('E', '', z_count).replace('R', '', z_count).replace('O', '', z_count)
        number[0] = z_count

    w_count = line.count('W')
    if w_count > 0:
        line = line.replace('T', '', w_count).replace('W', '', w_count).replace('O', '', w_count)
        number[2] = w_count

    x_count = line.count('X')
    if x_count > 0:
        line = line.replace('S', '', x_count).replace('I', '', x_count).replace('X', '', x_count)
        number[6] = x_count

    s_count = line.count('S')
    if s_count > 0:
        line = line.replace('S', '', s_count).replace('E', '', 2*s_count).replace('V', '', s_count).replace('N', '', s_count)
        number[7] = s_count

    v_count = line.count('V')
    if v_count > 0:
        line = line.replace('F', '', v_count).replace('I', '', v_count).replace('V', '', v_count).replace('E', '', v_count)
        number[5] = v_count

    g_count = line.count('G')
    if g_count > 0:
        line = line.replace('E', '', g_count).replace('I', '', g_count).replace('G', '', g_count).replace('H', '', g_count).replace('T', '', g_count)
        number[8] = g_count

    u_count = line.count('U')
    if u_count > 0:
        line = line.replace('F', '', u_count).replace('O', '', u_count).replace('U', '', u_count).replace('R', '', u_count)
        number[4] = u_count

    i_count = line.count('I')
    if i_count > 0:
        line = line.replace('N', '', 2*i_count).replace('I', '', i_count).replace('E', '', i_count)
        number[9] = i_count

    h_count = line.count('H')
    if h_count > 0:
        line = line.replace('T', '', h_count).replace('H', '', h_count).replace('R', '', h_count).replace('E', '', 2*h_count)
        number[3] = h_count

    number[1] = (len(line)//3)
    
    result = ''
    for i in range(0, 10):
        result += str(i)*number[i]
    return result



file = open(sys.argv[1]) #open('test.txt')
output = open('output.txt', 'w')
nTests = int(file.readline())

for testNb in range(1, nTests+1):     
    res = solveProblem(file)
    output.write(formatOutput(testNb, res))
    testNb += 1
