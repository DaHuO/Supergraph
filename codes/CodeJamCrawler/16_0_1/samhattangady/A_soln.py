#!/usr/bin/python
import sys

def main(q, a):
    ques = open(q, 'r')
    ans = open(a, 'w')

    for case in range(int(ques.readline().strip())):
        n = int(ques.readline().strip())
        b = n
        dig = set(str(n))
        for i in range(2,1000):
            if b == 0:
                break
            
            if len(dig) == 10:
                break
            
            n = b*i
            dig = dig.union(set(str(n)))
        if b == 0 or i==1000:
            ans.write('Case #{}: INSOMNIA\n'.format(case+1))
        else:
            ans.write('Case #{}: {}\n'.format(case+1, n))

    ques.close()
    ans.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
