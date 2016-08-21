def IsSetFull(set):
    for i in range(10):
        if i not in set:
            return False
    return True

def BreakDownToDigits(number):
    digits = set()
    while (True):
        digits.add(number % 10)
        number //= 10        
        if (number == 0):
            break
    return digits; 

def FindFinalSheep(number):
    if number == 0:
        return 'INSOMNIA'

    n = number;
    set = BreakDownToDigits(n)

    while (not IsSetFull(set)):
        n += number
        set = set.union(BreakDownToDigits(n))

    return str(n)


def main():

    f = open('A-large.in')
    out = open('A-large.out', 'w')
    
    caseNumber = int(f.readline())
    
    for i in range(1, caseNumber + 1):
        number = int(f.readline());
        result = FindFinalSheep(number)
        print('Case #' + str(i) + ': ' + str(number) + ' -> ' + result)
        out.write('Case #' + str(i) + ': ' + result + '\n');
    
    out.close()
    
    
if __name__ == '__main__':
    main()