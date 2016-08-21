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

def solve(line):
    MAX_ITER = 100
    seen = {'0': False, '1': False, '2': False, '3': False, '4': False,
            '5': False, '6': False, '7': False, '8': False, '9': False}

    number = int(line)
    for i in range(1, MAX_ITER + 1):
        loop_number = i * number
        str_number = str(loop_number)
        for j in range(len(str_number)):
            if seen[str_number[j]] == False:
                seen[str_number[j]] = True
            
        all_seen = True
        for k in range(10):
            if seen[str(k)] == False:
                all_seen = False
        if all_seen == True:
            return loop_number
    return "INSOMNIA"

if __name__ == "__main__":
    filename = "A-large.in"
    file = load_file(filename)
    n = int(file[0])
    #print(int(file[0]))
    out = []
    for i in range(1, n+1):
#        line = input()
        line = file[i]
        out.append("Case #{0}: {1}".format(i, solve(line)))
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