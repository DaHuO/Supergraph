
for l in range (int(input())):
     N = input()
     L = []
     n = 1
     result = ""
     if (N != '0'):
          while (len(L) < 10):
               result = str(n*int(N))
               L = list(set(''.join(L) + result))
               n += 1
     else:
          result = "INSOMNIA"
     print ("Case #{0}: {1}".format(l+1,result))

