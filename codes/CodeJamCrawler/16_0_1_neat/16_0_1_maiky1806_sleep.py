import sys

def print_result(numCase, result):
    print "Case #"+str(numCase)+":",result

def count_numbers(value, valChecked):
    digits = [int(i) for i in str(value)]
    for i in digits:
        valChecked[i]=1

#Read file pass by argument
lines = [line.rstrip('\n') for line in open(sys.argv[1])]

T = int(lines[0])

for numCase in range(1, T+1):
    case = int(lines[numCase])
    if(case == 0):
        print_result(numCase, "INSOMNIA")

    else:
        valChecked =[0 for i in range(10)]
        founded=False
        j=1
        while (not founded):
            value=case*j
            count_numbers(value, valChecked)
            if (sum(valChecked) == 10):
                founded=True
                print_result(numCase, value)
            j+=1