class Solution(object):
    #Solved using Pyth2.7
    def process2(self,num):
        i = 1; digits = []
        act = ['0','1','2','3','4','5','6','7','8','9']
        while 1:
            n = int(num)*i
            digits += list(str(n))
            ctr = 0
            for e in act:
                if e in digits:
                    ctr += 1
                    if ctr == 10:
                        return n
                else:
                    i += 1
                    break
            
    def process1(self):
        fin = open("A-large.in",'r')
        fout = open("outFile.txt",'w')
        line=fin.readline()
        line=fin.readline()
        lctr = 0
        while line != '':
            lctr += 1
            num = line.strip()
            if int(num) == 0:
                fout.write("Case #"+str(lctr)+':'+" INSOMNIA"+'\n')
            else:
                n = self.process2(num)
                fout.write("Case #"+str(lctr)+': '+str(n)+'\n')
            line=fin.readline()
        fin.close()
        fout.close()
                    

"__main__"
s=Solution()
s.process1()