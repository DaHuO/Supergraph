def find_all_numbers(line):
    line = list(line)
    result = []
    while "Z" in line:
        result.append(0)
        line.remove('Z')
        line.remove('E')
        line.remove('R')
        line.remove('O')
    while "W" in line:
        result.append(2)
        line.remove('T')
        line.remove('W')
        line.remove('O')
    while "U" in line:
        result.append(4)
        line.remove('F')
        line.remove('O')
        line.remove('U')
        line.remove('R')
    while "F" in line:
        result.append(5)
        line.remove('F')
        line.remove('I')
        line.remove('V')
        line.remove('E')
    while "X" in line:
        result.append(6)
        line.remove('S')
        line.remove('I')
        line.remove('X')
    for _ in range(line.count('V')):
        result.append(7)
    while "G" in line:
        result.append(8)
        line.remove('E')
        line.remove('I')
        line.remove('G')
        line.remove('T')
        line.remove("H")
    for _ in range(line.count('O')):
        result.append(1)
    for _ in range(line.count('R')):
        result.append(3)
    for _ in range(line.count('I')):
        result.append(9)
    return result



cases_number = int(input())
for case in range(1, cases_number+1):
    phone = []
    phone_string = input()
    phone = find_all_numbers(phone_string)
    phone.sort()
    print("Case #" + str(case) + ": " + ''.join(map(str, phone)))