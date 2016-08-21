#!/usr/bin/python
# -*- coding: utf-8 -*-

def to_digits(N):
    NN = N
    digits = set()
    while NN>0:
        digits.add(NN%10)
        NN = int(NN/10)
    return digits

def main():
    in_file = open("A-large.in", mode='r')
    out_file = open("A-large.out", mode='w')

    lines = in_file.readlines()      
    T = int(lines[0])
    
    for i in xrange(T):
        line = lines[i + 1]
        N = int(line)
        
        if N==0:
            out_file.write("Case #" + str(i+1) + ": " + "INSOMNIA" + "\n") 
            continue
            
        digits = set()
        
        j = 0
        while len(digits) < 10:
            j += 1
            digits = digits.union(to_digits(j*N))
                
        out_file.write("Case #" + str(i+1) + ": " + str(j*N) + "\n") 
        
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
