#!/bin/python
f = open('test.txt', 'r')
output = open('output.txt', 'w')

c = 0

for line in f:
    if c == 0:
        c+= 1
    else:
        start = int(line)
        digits = []
        for i in range(0, 10):
            digits.append(False)

        counter = 1
        number = start*counter
    
        # main loop
        while(False in digits):
            # 2**32 = 10 digits
            for i in range(0, 20):
                if number >= 10**i:
                    temp = int((number//(10**i))%10)
                    # print((number//(10**i))%10)
                    digits[temp] = True
            print('number={}: {}'.format(number, digits))
            counter += 1
            if number == start*counter:
                counter = -1
                break
            if number > 2**64:
                counter = -1
                break
            number = start*counter
        if counter != -1:
            output.write('Case #{}: {}\n'.format(c, start*(counter-1)))
        else:
            output.write('Case #{}: INSOMNIA\n'.format(c))
        print('Case #{}:   {} ->  {}'.format(c, start, start*(counter-1)))
        c += 1


f.close()
output.close()
