def flip(x,y,strng):
    j = x
    while(j<y):
        if(strng[j]=="+"):
            strng[j]="-"
        else:
            strng[j]="+"
        j+=1
    return strng
        
cnt = input()
i = 1
while(i <= cnt):
 flips = 0
 cookie = raw_input()
 dic = list(reversed(cookie))
 k = 0
 while(k < len(dic)):
     if(dic[k]=="-"):
         dic = flip(k,len(dic),dic)
         flips += 1
     if(all(sym == "+" for sym in dic)):
         break
     else:
         k += 1
 print "Case #{0}: {1}".format(i,flips)
 i +=1
