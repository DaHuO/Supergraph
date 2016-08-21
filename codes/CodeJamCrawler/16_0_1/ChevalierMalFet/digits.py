inputF = open('A-large.in', 'r')
output = open('A-large.out', 'w')

numCases = int(inputF.readline())

for i in range(numCases):
    n = int(inputF.readline())
    if n == 0:
        output.write('Case #' + str(i+1) + ': ')
        output.write('INSOMNIA' + '\n')
        continue
    
    j = 0
    digits = [0]*10
    while sum(digits) < 10:
        j += 1
        strNum = str(j*n)
        for digit in strNum:
            digits[int(digit)] = 1

    output.write('Case #' + str(i+1) + ': ')
    output.write(strNum + '\n')
        

    
    

inputF.close()
output.close()
