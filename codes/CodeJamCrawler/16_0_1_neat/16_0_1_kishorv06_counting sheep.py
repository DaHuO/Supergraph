cnt = input()
i = 1
while(i <= cnt):
 num = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
 n = input()
 j = 1
 while(1):
     digits = list(str(j*n))
     for digit in digits:
         num[digit] += 1
     if(all(v > 0 for v in num.itervalues())):
        print "Case #{0}: {1}".format(i,j*n)
        break
     elif(any(v > 1000000 for v in num.itervalues())):
         print "Case #{0}: {1}".format(i,"INSOMNIA")
         break
     j +=1
 i +=1
