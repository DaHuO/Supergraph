t = int(input()) 
for i in range(1, t + 1):
  
  n = int(input())
  if n == 0:
    result = "INSOMNIA"
  
  else:
    x = set([0,1,2,3,4,5,6,7,8,9])
    j = 1

    while len(x) > 0:    
      result = n*j

      for d in list(str(result)):
        x.discard(int(d))

      j += 1

  print("Case #{}: {} ".format(i, result))