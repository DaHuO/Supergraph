# -*- coding: utf-8 -*-
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import copy
def load_file(filename):
    in_file = open(filename, encoding='utf-8')
    content = in_file.readlines()
    return content

def writeStringToFile(output, filename):
    out_file = open(filename + '.out', 'w')
    for i in output:
        out_file.write(i + '\n')
    out_file.close()

def solve(line):
    string = line.split()[0]
    size = len(string)
    all_strings = [string[0]]
    for i in range(1, size):
        other_str = copy.copy(all_strings)
        for j in range(len(all_strings)):
            all_strings[j] += string[i]
        for k in range(len(other_str)):
            temp = other_str[k]
            other_str[k] = string[i] + temp
        all_strings += other_str
    all_strings.sort()

    return all_strings[len(all_strings)-1]

if __name__ == "__main__":
    filename = "A-small-attempt0.in"
    file = load_file(filename)
    n = int(file[0])
#    print(int(file[0]))
    out = []
    for i in range(1, n+1):
        line = file[i]
        out.append("Case #{0}: {1}".format(i, solve(line)))
#print(out)
writeStringToFile(out, filename)



