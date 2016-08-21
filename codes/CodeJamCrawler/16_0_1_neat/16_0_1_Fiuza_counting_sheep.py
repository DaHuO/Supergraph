import sys

def countingSheep(case, line) :
    if case == 0 :
        return
    final = range(0, 10)
    i = int(line)
    N = 0
    digits = []
    numbers = []
    while True :
        N += 1
        number = N * i
        for digit in str(number) :
            digit = int(digit)
            if digit not in digits :
                digits.append(int(digit))
        if number in numbers :
            print("Case #%d: INSOMNIA" % case)
            break
        elif set(range(10)) == set(digits) :
            print("Case #%d: %d" % (case, number))
            break
        numbers.append(number)
def main() :
    with open(sys.argv[1], 'r') as f :
        ln = 0
        for line in f :
            countingSheep(ln, line.rstrip())
            ln += 1

if __name__ == "__main__" :
    main()
