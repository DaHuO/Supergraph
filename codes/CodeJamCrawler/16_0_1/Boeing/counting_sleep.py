#!/bin/python
import sys
if __name__ == '__main__':
    input_name = sys.argv[1] 
    output_name = sys.argv[2] 
    f = open(input_name, 'r')
    f2 = open(output_name, 'w')
    nb_cases = int(f.readline().strip())
    for i in range(1, nb_cases+1):
        print 'case ' + str(i)
        number = int(f.readline().strip())
        s = set()
        ss = 0
        if number:
            while len(s) != 10:
                ss += number
                s = s.union(set(map(int, str(ss))))
        f2.write('Case #' + str(i) + ': ') 
        if len(s) == 0:
            f2.write('INSOMNIA\n')
        else:
            f2.write(str(ss) + '\n')
    f.close()
    f2.close()
