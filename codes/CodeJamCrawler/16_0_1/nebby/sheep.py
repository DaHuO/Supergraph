import sys
inputs = sys.stdin.readline()
for x in range(int(inputs)):
    line = sys.stdin.readline()
    num = int(line)
    if(num==0):
        print('CASE #' + str((x+1)) + ': INSOMNIA')
    else:
        digits = {}
        multiplier = 0
        while len(digits) < 10:
            multiplier += 1
            line = str(num*multiplier)
            for digit in line:
                if(digit not in digits):
                    digits[digit] = True
        print('CASE #' + str((x+1)) + ': ' + str(multiplier * num))
