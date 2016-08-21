

if __name__ == '__main__':
    with open('a.txt','r+') as fin:
        with open('a.out','w+') as fout:
            n = fin.readline().strip()
            cc = 0
            for i in range(int(n)):
                cc += 1
                print >>fout, 'Case #%d:'%(cc),
                cake = fin.readline().strip()
                cake = cake.replace('+','1')
                cake = cake.replace('-','0')
                cake = cake[::-1]
                st = 0
                en = len(cake) - 1
                ans = 0
                choco = 1
                while (len(cake) > 0 and st <= en):
                    if int(cake[st]) == choco:
                        st += 1
                        continue
                    else:
                        flag = (int(cake[en]) == choco)
                        while (int(cake[en]) == choco):
                            en -= 1
                        if st == 0:
                            cake = cake[en::-1]
                        else:
                            cake = cake[en:st-1:-1]
                        ans += 1 + flag
                        choco = 1 - choco
                        st = 0
                        en = len(cake) -1 
                        
                print >> fout, ans
                
            