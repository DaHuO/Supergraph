

if __name__ == '__main__':
    with open('a.txt','r+') as fin:
        with open('a.out','w+') as fout:
            n = fin.readline().strip()
            cc = 0
            for i in range(int(n)):
                cc += 1
                print >>fout, 'Case #%d:'%(cc),
                k = int(fin.readline().strip())
                if k == 0:
                    print >>fout,'INSOMNIA'
                    continue
                index = {}
                count = 0
                for j in range(1,1000):
                    t = str(j*k)
                    for c in t:
                        if not index.has_key(c):
                            count += 1
                            index[c] = 1
                            if count == 10:
                                break
                    if count == 10:
                        print >>fout, k * j
                        break
                
            