import math
 
def Factor(number, limit):
    lim = min(math.ceil(math.sqrt(number)), limit, number - 1)
    for i in range(2, lim + 1):
        if (number % i == 0):
            return (False, i)
    return (True, 0)


def ToBinaryString(number):
    digits = [];
    while(True):
        digits.insert(0, number % 2)
        number //= 2;
        if (number == 0):
            break;

    return digits;

def InterpretDigitsAsSystem(digits, system):
    power = 1;
    sum = 0;    
    for digit in reversed(digits):
        sum += power * digit
        power *= system

    return sum

def DigitsToStr(digits):
    s = ''
    for i in digits:
        s += str(i)
    return s


def IsDigitsJamcoin(digits):

    if (len(digits) == 0):
        return ('', [])

    if (digits[0] != 1) or (digits[len(digits) - 1] != 1):
        return ('', [])

    isPrime = False;
    factors = [];
    for j in range(2, 11):
        number = InterpretDigitsAsSystem(digits, j)
        (res, factor) = Factor(number, 10000)
        if (res):
            isPrime = True
            break;
        else:
            factors.append(factor)
        
    if (not isPrime):
        return (DigitsToStr(digits), factors)
    else:
        return ('', [])

def FactorsToStr(lst):
    s= ' '.join([str(i) for i in lst])
    return s


def MineJamCoins(left, right, max):

    count = 0
    checked = 0
    jamcoins = []
    for i in range(left, right, 2):
        #print('iteration = ' + str(checked))
        checked += 1
        digits = ToBinaryString(i)
        (bits, factors)= IsDigitsJamcoin(digits)

        if (len(bits) != 0):
            count += 1;
            jamcoin = bits + " " + FactorsToStr(factors)
            print('jamcoin #'+ str(count) + ': '+ jamcoin)
            jamcoins.append(jamcoin)

        if (count == max):
            print('checked = '+ str(checked))
            break

    return jamcoins




def main():

    #print (IsDigitsJamcoin([1, 0, 1]))
    #print (IsDigitsJamcoin([1, 0, 0, 1]))

    #print (IsDigitsJamcoin([1, 0, 0, 0, 1, 1]))
    #print (IsDigitsJamcoin([1, 1, 1, 1, 1, 1]))
    #print (IsDigitsJamcoin([1, 1, 1, 0, 0, 1]))

    
    

    #f = open('test.in')
    out = open('testlarge.out', 'w')
    out.write('Case #1:\n');
    #jamcoins = MineJamCoins(32769, 65536, 50)
    jamcoins = MineJamCoins(2**31 + 1, 2**32, 500)
    for jc in jamcoins:
        out.write(jc + '\n');


    
    #caseNumber = int(f.readline())
    
    #for i in range(1, caseNumber + 1):
    #    number = int(f.readline());
    #    result = FindFinalSheep(number)
    #    print('Case #' + str(i) + ': ' + str(number) + ' -> ' + result)
    #    out.write('Case #' + str(i) + ': ' + result + '\n');
    
    #out.close()
    
    
if __name__ == '__main__':
    main()