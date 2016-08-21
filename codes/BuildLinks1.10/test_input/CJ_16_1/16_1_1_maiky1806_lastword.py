import sys

def print_result(numCase, result):
    print "Case #"+str(numCase)+":",result


#Read file pass by argument
lines = [line.rstrip('\n') for line in open(sys.argv[1])]

T = int(lines[0])

for numCase in range(1, T+1):
    letters = [v for v in lines[numCase]]
    result=letters[0]
    previous=letters[0]
    for i in range(1, len(letters)):
        if letters[i] >= result[0]:
            result = letters[i]+result
        else:
            result += letters[i]
        previous= letters[i]

    print_result(numCase, result)