T = int(input())
for x in range(1, T + 1):
   N = int(input())
   number = ''
   i = 1
   pro = 0
   if N==0:
      print("Case #{}: {} ".format(x,"INSOMNIA"))
   else:
      while True:
         pro = N * i
         y=str(pro)
         for j in y:
            if j not in number:
              number+=j
         if len(number)==10:
           break
         i += 1
      print("Case #{}: {} ".format(x,pro))
