f = open("input.txt","r+")
w = open("output.txt","w")
t = int(f.readline())

d = {0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}
for a0 in range(1,t+1):
    res = []
    fin = []
    s = f.readline()
    zero = s.count('Z')
    #print "Zero" 
    two = s.count('W')
    #print "two"
    four = s.count('U')
    six = s.count('X')
    eight = s.count('G')
    one = s.count('O')-zero-two-four
    three = s.count('H')-eight
    five = s.count('F')-four
    seven = s.count('V')-five
    nine = s.count('I')-five-six-eight
    res.append(zero)
    res.append(one)
    res.append(two)
    res.append(three)
    res.append(four)
    res.append(five)
    res.append(six)
    res.append(seven)
    res.append(eight)
    res.append(nine)
    print res

    res = [zero,one,two,three,four,five,six,seven,eight,nine]
    for i in range(0,len(res)):
        if(res[i]>=1):
            for j in range(0,res[i]):
                fin.append(i)
    r = ''
    for i in range(0,len(fin)):
        r+= (str(fin[i]))
    print r
    wr = "Case #%d: %s\n"%(a0,r)
    w.write(wr)
    
    #s = f.readline()
    

f.close()
w.close()












'''s = "Case #%d: "%(a0)
    fout.write(s)
    for i in range (n):
        fout.write(res[i])'''
