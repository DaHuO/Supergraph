import fileinput
import math


def int2base(i, base):
    o = []
    order = 1
    k = base
    o.append(i % base)
    i /= base
    while i != 0:
        o.append(i % base)
        i /=  base
    
    o = o[::-1]
    return o
    

def digits2int(digits,  base):
    n = 0
    k = 1
    for i in digits[::-1]:
        n += k * i
        k *= base
    return n

def main():
    # inputs = [0, 1, 2, 11, 1692]
    inputs = []
    
    for line in fileinput.input():
        inputs.append(line.strip())
    line = inputs[-1]
    N, J = tuple(map(int, line.split()))
    outputs = []
    digits = [1] + [0] * (N-2) + [1]

    i = 0
    print 'Case #1:'
    while len(outputs) < J:
        output = []
        base2 = int2base(i, 2)
        digits[-1-len(base2):-1] = base2
        output.append(''.join(map(str, digits)))

        for base in xrange(2, 11):
            done = False
            num = digits2int(digits, base)
            for j in [2,3,5,7,11,13,17,19]:
                if num % j == 0:
                    output.append(j)
                    done = True 
                    break
            if not done:
                break
        
        if len(output) == 10:
            outputs.append(output)
            # print len(outputs),
            print ' '.join(map(str,output))

        i += 1




            

if __name__ == '__main__':
    main()
