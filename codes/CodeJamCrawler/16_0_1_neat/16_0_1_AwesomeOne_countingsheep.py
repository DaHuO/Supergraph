# python2

fin = open('A.in' , 'r')
fout = open('A.out' , 'w')
T = fin.readline()
T = int(T)

for t in range(1 , T+1):
    N = fin.readline()
    N = int(N)
    l = [0]*10
    if N == 0:
        fout.writelines('Case #'+str(t)+': INSOMNIA\n')
    else:
        i = 1
        while True:
            temp = i * N
            while temp:
                mo = temp % 10
                temp = temp / 10
                if l[mo] == 0:
                    l[mo] = 1
            if 0 in l:
                i += 1
                continue
            else:
                break
        fout.writelines('Case #'+str(t)+': '+str(i*N)+'\n')

            
fin.close()
fout.close()
