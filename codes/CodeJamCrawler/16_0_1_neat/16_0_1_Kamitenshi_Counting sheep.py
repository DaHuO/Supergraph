def tests(digits):
    i = 0
    while i < len(digits) and digits[i] == True:
        i += 1
    return i == len(digits)



def counting(number):
    if number == 0:
        return "INSOMNIA"
    digits = [False] * 10
    i = 0
    while not (tests(digits)):
        i += 1
        case = number * i
        while case > 9 :
            digits[case % 10] = True
            case //= 10
        digits[case] = True
    return number * i

def main():
    f = open("A-large.in", "r")
    w = open("Result_large.in", "w")
    cases = int(f.readline())
    for case in range (cases):
        number = int(f.readline())
        result = counting(number)
        w.write("Case #" + str(case + 1) + ": " + str(result) + "\n")
    f.close()
    w.close()

main()
