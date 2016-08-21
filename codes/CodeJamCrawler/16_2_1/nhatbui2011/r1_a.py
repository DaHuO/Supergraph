def main():
    file = open('in.txt', 'r')
    data = file.read()
    file.close()

    lines = data.split("\n")
    n = int(lines[0])
    result = ''
    for i in range(1, n + 1):
        ret = solve(lines[i])
        result += 'Case #' + str(i) + ': ' + ret + "\n"

    file = open('out.txt', 'w')
    file.write(result)
    file.close()


def solve(s):
    a = []
    while 'Z' in s:
        a.append(0)
        s = s.replace('Z', '', 1).replace('E', '', 1).replace('R', '', 1).replace('O', '', 1)
    while 'W' in s:
        a.append(2)
        s = s.replace('T', '', 1).replace('W', '', 1).replace('O', '', 1)
    while 'U' in s:
        a.append(4)
        s = s.replace('F', '', 1).replace('O', '', 1).replace('U', '', 1).replace('R', '', 1)
    while 'X' in s:
        a.append(6)
        s = s.replace('S', '', 1).replace('I', '', 1).replace('X', '', 1)
    while 'G' in s:
        a.append(8)
        s = s.replace('E', '', 1).replace('I', '', 1).replace('G', '', 1).replace('H', '', 1).replace('T', '', 1)
    while 'O' in s:
        a.append(1)
        s = s.replace('O', '', 1).replace('N', '', 1).replace('E', '', 1)
    while 'R' in s:
        a.append(3)
        s = s.replace('T', '', 1).replace('H', '', 1).replace('R', '', 1).replace('E', '', 1).replace('E', '', 1)
    while 'F' in s:
        a.append(5)
        s = s.replace('F', '', 1).replace('I', '', 1).replace('V', '', 1).replace('E', '', 1)
    while 'S' in s:
        a.append(7)
        s = s.replace('S', '', 1).replace('E', '', 1).replace('V', '', 1).replace('E', '', 1).replace('N', '', 1)
    while len(s) > 0:
        a.append(9)
        s = s.replace('N', '', 1).replace('I', '', 1).replace('N', '', 1).replace('E', '', 1)

    a.sort()
    return ''.join(str(x) for x in a)

main()