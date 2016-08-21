DIGITS = [0,1,2,3,4,5,6,7,8,9]
FILEPATH = "E:\Downloads\A-large.in"

def insomnia(number, count = 1, digits = []):
    n = number * count
    digits = addDigitsToList(digits[:], n)
    if set(digits) == set(DIGITS):
        return str(number * count)
    if number * (count+1) == number:
        return str("INSOMNIA")
    res = insomnia(number, count+1, digits)
    return res

def addDigitsToList(digits, number):
    while number > 0:
        digits.append(number % 10)
        number /= 10
    return list(set(digits))
    
def solve(filepath = ""):
    c = -1
    if filepath == "" or filepath == None:
        filepath = FILEPATH
    with open(filepath) as f:
        for line in f:
            if c == -1:
                c = 1
                continue
            result = insomnia(int(line))
            print ("Case #"+str(c)+": "+str(result))
            c += 1
            
