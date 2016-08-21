def main():
    T = int(raw_input())
    
    for t in range(1, T + 1):
        N = int(raw_input())
        digitsLeft = set(getDigits('0123456789'))
        i = 1
        result = 0
        while True:
            result = i * N
            digitsLeft = digitsLeft - getDigits(result)
            i = i + 1
            if result == 0:
                result = 'INSOMNIA'
                break
            if not digitsLeft:
                break
        print ("Case #" + str(t) + ": " + str(result))
            
        
def getDigits(number):
    digits = []
    for digit in str(number):
        digits.append(digit)
    return set(digits)
        
main()