
def insertDigit(digit, digits):
    if digit not in digits:
        digits.append(digit)

def getDigits(number, digits):
    lastDigit = False
    auxNumber = number
    while(not lastDigit):
        digit = auxNumber % 10
        rest = auxNumber / 10
        insertDigit(digit, digits)
        if len(digits) == 10:
            return True


        if rest == 0:
            lastDigit = True 

        auxNumber = rest
    return False

def whenSleep(number, digits):
    number = int (number)
    if number == 0:
        return 'INSOMNIA'
    i = 1
    sleep = False
    while(not sleep):
        newNumber = number * i
        i += 1
          
        if getDigits(newNumber, digits):
            return newNumber 
        if i >= 1000000:
            sleep = True
    return 'INSOMNIA'



if __name__ == '__main__':
    
    nTestCases = int(raw_input())
    
    for i in range(0, nTestCases):
        digits = []
        bleatrixNumber = raw_input()
        response = whenSleep(bleatrixNumber, digits)
        print 'Case #%s: %s' % (i + 1, response)
