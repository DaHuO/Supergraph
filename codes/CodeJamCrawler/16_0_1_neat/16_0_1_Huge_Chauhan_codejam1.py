# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
   n=int(input())
   k=1
   x=''
   r=0
   if n==0:
      print("Case #{}: {} ".format(i,"INSOMNIA"))   
   else:
      while True:
         r=n*k
         y=str(r)
         for j in y:
            if j not in x:
              x+=j
         if len(x)==10:
           break
         k+=1
      print("Case #{}: {} ".format(i,r))
