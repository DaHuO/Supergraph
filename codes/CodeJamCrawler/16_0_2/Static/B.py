# -*- coding: utf-8 -*-
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def load_file(filename):
    in_file = open(filename, encoding='utf-8')
    content = in_file.readlines()
    return content

def writeStringToFile(output, filename):
    out_file = open(filename + '.out', 'w')
    for i in output:
        out_file.write(i + '\n')
    out_file.close()

def flip(stack, i):
    #print(stack, i)
    size = len(stack)
    new_stack = ""
    for j in range(i):
        if stack[j] == '-':
            new_stack += '+'
        else:
            new_stack += '-'
    new_stack += stack[i:size]
    #print(new_stack)
    return new_stack
        
def solve(line):
    stack = line.split()[0]
    size = len(stack)
    count = 0
    for i in range(size):
        if stack[size - i - 1] == '-':
            stack = flip(stack, size - i)
            count += 1
    return count

if __name__ == "__main__":
    filename = "B-large.in"
    file = load_file(filename)
    n = int(file[0])
    #print(int(file[0]))
    out = []
    for i in range(1, n+1):
        line = file[i]
        out.append("Case #{0}: {1}".format(i, solve(line)))
#print(out)
writeStringToFile(out, filename)


#def load_file(filename):
#    in_file = open(filename, encoding='utf-8')
#    test_cases = in_file.readline().strip().split()
#    print(test_cases)
#    cases_data = []
#    for i in range(test_cases):
#        cases_data.append(list(in_file.readline().strip()))
#    in_file.close()
#    return test_cases, cases_data
#

#
## Read a file
#test_cases, cases_data = load_file("A-small.in")
#out = []
#MAX_ITER = 10
#
#for i in range(MAX_ITER):
#  print(i)
#  out.append("Case #{}: {} {}".format(i, i, i)) 
#print(out)
#writeStringToFile("A-small.out")