fp_in = open('A-large.in', 'r+')
fp_out = open('out.txt', 'w+')
T = fp_in.readline()
T = int(T)


for x in range(1, T+1, 1):
    w = fp_in.readline()
    w = w.split('\n')[0]
    i = 1
    sheep =int(w)
    all = ''
    if sheep<1:
        #print('Case #%d: INSOMNIA\r' %x)
        fp_out.write('Case #%d: INSOMNIA\r' %x)
        continue

    #count=len(set(str(i*int(sheep))))
    while(1):
        all =all +str(i*sheep)
        count=len(set(str(all)))
        if count==10:
            #print('Case #%d: %d\r' %(x, i*sheep))
            fp_out.write('Case #%d: %d\r' %(x, i*sheep))
            break
        else:
            i=i+1


fp_in.close()
fp_out.close()