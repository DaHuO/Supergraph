def number_of_flips(string, flag):
    dash = string.rfind('-')
    plus = string.rfind('+')
    if dash == -1:
        return int(not flag)
    if plus == -1:
        return int(flag)
    if plus > dash:
        return number_of_flips(string[:dash+1], not flag) + int(not flag)
    if dash > plus:
        return number_of_flips(string[:plus+1], not flag) + int(flag)

def get_flips(string):
    index = string.rfind('-')
    substring = string[:index+1]
    return number_of_flips(substring, True)

def pancake_revenge(filename):
    file = open(filename, 'r')
    source = file.read()
    file.close()
    file = open('pancake_revenge.txt', 'w');
    lines = source.splitlines()
    T = int(lines[0])
    for i in range(T):
        string = lines[i+1]
        file.write('Case #' + str(i+1) + ': ' + str(get_flips(string)) + '\n')


pancake_revenge('B-large.in')
