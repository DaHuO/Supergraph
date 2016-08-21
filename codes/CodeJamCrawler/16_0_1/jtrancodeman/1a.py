

output = open('1a-large.out','w')

with open('1A-large.in','r') as input:
    for i in range(int(input.readline())):
        digits = [0]*10
        base = int(input.readline())
        if base == 0:
            output.write('Case #' + str(i+1) + ': INSOMNIA\n')
        else:
            a = 1
            while sum(digits) < 10:
                s = base*a
                for d in str(s):
                    digits[int(d)] = 1
                a += 1

            output.write('Case #' + str(i+1) + ': ' + str(s) + '\n')
output.close()

        
