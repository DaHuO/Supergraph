from collections import Counter

output = open('test.out', 'w')

def is_empty(ls):
    for x in ls:
        if ls[x] ==1:
            return True
    return False

#number of test cases

f = open('A-large.in')
case = int(f.readline())
#output. write('')

for c in range(1, case+1):
    test = int(f.readline())
    if test == 0:
        output.write('Case #1: INSOMNIA\n')
        print('Case #1: INSOMNIA')
    else:
        digits = Counter('0123456789')
        i = 1
        while i:
            y = i*test
            i += 1
            digits.update(str(y))
            if is_empty(digits) == False:
                output.write('Case #' + str(c) + ': ' +str(y) + '\n')
                print ('Case #' + str(c) + ': ' +str(y)  )
                break





#Case #1: Insomnia
