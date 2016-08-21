#Read the number of test cases
N = input()

#Read in the inputs
inputs = []
for x in range(N):
    line = input()
    inputs.append(line)

#Returns the number of times the input needs to be multiplied by 2
#So that every digit will appear, or 'INSOMNIA' for 0
def calculate(start):
    if start==0:
        return 'INSOMNIA'

    #Array of digits 0-9
    digits = range(10)

    #Keep mulitplying by m until all digits have occurred
    n = 0
    while 1:
        case = start * (n+1)
        numbers = [int(x) for x in str(case)]
        for i in numbers:
            if i in digits:
                digits.remove(i)
        if not digits:
            return case
        n = n+1

#Calculate the output for each input case
k = 1
for case in inputs:
    result = str(calculate(case))
    print "Case #"+str(k)+": "+result
    k += 1
