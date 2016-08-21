filename = open("ain.txt")
out = open("aout.txt",'w')

       
t = int(filename.readline())

i=0
while i<t:
        i += 1

        word = filename.readline().strip()
        v = [0,0,0,0,0,0,0,0,0,0]
        v[0] = word.count('Z')
        v[2] = word.count('W')
        v[6] = word.count('X')        
        v[4] = word.count('U')
        v[5] = word.count('F')-v[4]
        v[8] = word.count('G')
        v[3] = word.count('H')-v[8]
        v[1] = word.count('O')-v[0]-v[2]-v[4]
        v[9] = word.count('I')-v[5]-v[6]-v[8]
        v[7] = word.count('V')-v[5]

       
                        
        res = ''

        j = 0
        while j<10:
                k = 0
                while k<v[j]:
                        res = res + str(j)
                        k += 1
                j += 1
        
        out.write('Case #'+str(i)+': '+res)
        out.write('\n')
