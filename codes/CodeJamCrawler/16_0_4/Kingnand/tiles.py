'''
Created on Apr 9, 2016

@author: kingnand
'''
import sys

def clean_tiles_2(k, c, s=None):
    if s is None:
        s=k
    arr=[]
    for i in range(k):
        arr.append(i*(k**(c-1)))
        i+=1
    return arr            


def get_digit_at(num, ith):
    ith-=1
    return (num/(10**ith))%10

if __name__ == '__main__':
    with open('output.txt', 'w') as out:
        with open('D-small-attempt1.in', 'r') as f:
            num=0
            i=0
            for line in f:
                if i==0:
                    num=int(line)
                else:
                    parts = line.split(' ')
                    res = clean_tiles_2(int(parts[0].strip()), int(parts[1].strip()), int(parts[2].strip()))
                    if i > num:
                        sys.exit()
                    out.write('Case #' + str(i) + ': ')
                    if res is None:
                        out.write('IMPOSSIBLE\n')
                    else:
                        out.write(' '.join([str(j+1) for j in res]) + '\n')
                     
                i+=1
    pass
