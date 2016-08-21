i_file = open("A-large.in","r")
inputs = [line.rstrip('\n') for line in i_file]
i_file.close()
o_file = open("o1.out","w")
cases=1
del inputs[0]
for n in inputs:
    map={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    if n=="0":
        #print "INSOMNIA"
        o_file.write("Case #"+str(cases)+": INSOMNIA"+"\n")
        cases += 1
    else:
        num = int(n)
        while(True):
            for digit in n:
                if map[digit] == 0:
                    map[digit]=1
            if sum(map.values()) == 10:
                o_file.write("Case #"+str(cases)+": "+n+"\n")
                cases += 1
                #print n
                break
            else:
                n=(int(n)) + num
                n = str(n)
o_file.close()                  
