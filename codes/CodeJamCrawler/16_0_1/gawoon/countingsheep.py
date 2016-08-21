from sets import Set


def checkDigits(number, digits):
    if ( len(digits) == 0 ):
        return True

    while( number > 0 ):
        digit = number%10
        number = number/10
        if ( digit in digits ):
            #print digit
            digits.remove( digit )

    if ( len(digits) == 0 ):
        return True
    else:
        return False

def checkInsomnia(initnum):
    "Check Insomnia"
    digits = Set([0,1,2,3,4,5,6,7,8,9])
    find = False
    for N in range(1,1000000):
        number = N * initnum
        #print str(number) + '/ i * N: ' + str(N) + ' * ' + str(number)
        if checkDigits(number, digits):
            find = True
            break

    if find == True:
        return str(number)
    else:
        return "INSOMNIA"

f = open ( "./A-large.in", 'r' )
foutput = open ( "./output_large.txt", 'w')
T = int(f.readline())
if T >= 1 and T <= 100:
    i = 1
    while True:
        input = f.readline()
        if not input:
            break

        number = int(input)
        answer = checkInsomnia(number)
        output = 'Case #'+ str(i) + ': ' + answer + '\n'
        foutput.write(output)
        i = i+1
else:
    print('Limits Invalid')

f.close()
foutput.close()
