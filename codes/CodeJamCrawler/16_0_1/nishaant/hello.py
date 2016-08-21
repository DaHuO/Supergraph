inp = open('input1.txt','r+')
t = int (inp.readline())
out = open('output1.txt','w')
cou = 0;
while(t):
   cou = cou + 1
   t = t-1
   n = int (inp.readline())
   if n == 0:
      out.write("Case #"+str(cou)+": INSOMNIA\n")
   else :
      arr = [0] * 10
      k = n
      l = 1
      while(1):
         l = l + 1
         while(k>0):
             arr[k%10] = 1
             k = k/10
         c=1
         for i in range(0,10):
              if arr[i] == 0:
                  c=0
                  break

         if c==1:
            out.write("Case #"+str(cou)+": "+str((l-1)*n) + "\n")
            break
         else :
             k = l * n
out.close()
