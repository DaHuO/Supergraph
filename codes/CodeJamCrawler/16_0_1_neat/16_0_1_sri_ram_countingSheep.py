def countingSheep(filename):
    f=open(filename,'rU')
    tc=int(f.readline())
    g=open('countingSheepLarge.out','w')

    for i in range(tc):
        number=int(f.readline())
        trotter=set(str(number))
        incre=1
        sleep=False
        if len(trotter)==10:
            g.write(('Case #%d: %d\n')%(i+1,incre*number))
            continue
        elif number==0:
            g.write(('Case #%d: INSOMNIA\n')%(i+1))
        else:
            while not sleep:
                if len(trotter)==10:
                    sleep=True
                    g.write(('Case #%d: %d\n')%(i+1,incre*number))
                else:
                    incre+=1
                    trotter=trotter.union(set(str(incre*number)))
    g.close()
countingSheep('A-large.in')
