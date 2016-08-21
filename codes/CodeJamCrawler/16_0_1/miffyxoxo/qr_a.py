# -*- coding: utf-8 -*-

# QR A.  Counting Sheep

#INPUT = 'qr_a-smaii.in'
#OUTPUT = 'qr_a-small.out'
INPUT = 'qr_a-large.in'
OUTPUT = 'qr_a-large.out'

#LIMIT = 200
LIMIT = 10**6

def result(caseno, msg):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %s\n' % (caseno, msg))
    output.close()

def main():
    input = open(INPUT, 'r')

    case = int(input.readline().replace('\n',''))    # 1行目問題数
    
    for caseno in range(1, case+1):
        N = int(input.readline().replace('\n',''))
        
        if N == 0:
            result(caseno, 'INSOMNIA')
            continue
        
        count = 1
        digits = [0]*10
        while True:
            d = N * count
            for _d in str(d):
                digits[int(_d)] = 1

            if sum(digits) == 10:
                result(caseno, d)
                break

            count += 1

            if count > 200:
                result(caseno, 'INSOMNIA')
                break

if __name__ == '__main__':
    main()
