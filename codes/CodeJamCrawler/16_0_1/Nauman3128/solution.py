
import sys
from optparse import OptionParser

usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
elif not sys.stdin.isatty():
    f = sys.stdin
else:
    parser.error("Need input from file or stdin")
    

inputs = int(f.readline())
attempt_num = 1
attempted = 1
list_of_inputs = []
for i in range(0,int(inputs)):
    list_of_inputs.append(f.readline().strip())

for num in list_of_inputs:                            
    not_visited = True
    file = open("output.txt", "a")
    x = 1
    y = num
    result = 1
    res = ''
    l_out = []
    if int(y) == 0:   
        output = "Case #%s: INSOMNIA" % attempt_num
        file.write(output)
        file.write("\n")
        print output
        attempt_num +=1 
        continue
    while not_visited:
        res = res + str(result)
        out = set(res)
        l_out = list(out)
        if len(l_out) == 10:
            not_visited = False
            output = "Case #%s: %s" % (attempt_num, result)
            file.write(output)
            file.write("\n")
            print output
        else:
            result = int(y) * int(x)
            x = x + 1
    attempt_num += 1
    file.close()
    


