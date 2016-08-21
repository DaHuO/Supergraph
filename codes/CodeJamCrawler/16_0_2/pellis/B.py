import numpy as np

filename = 'BL'
fin = open(filename+'.in', 'r')
fout = open(filename+'.out', 'w')

for i in range(int(fin.readline().strip())):
    tmp = fin.readline().strip().split(' ')
    stack = tmp[0]
    n = 0
    while ('-' in stack):
        print(stack)
        end = stack.rindex('-')+1
        if(stack[0] == '+'):
            truc = stack.index('-')
            stack = ('-'*i)+stack[truc:]
            n += 1
        else:
            stack = stack[:end][::-1].replace('+', '0').replace('-', '+').replace('0', '-')+stack[end:]
            n += 1

    res = 'Case #'+str(i+1)+': '+str(n)+'\n'
    fout.write(res)
    print (res)
        
fout.close()
fin.close()