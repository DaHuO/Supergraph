prime = [2]
number= 3
point = 0
stop  = prime[point]**2
while len(prime)<65536:
    if stop<=number:
        point+=1
        stop=prime[point]**2
    for x in prime[:point]:
        if number%x==0:
            break
    else:
        prime.append(number)
    number+=1
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check(N):
     triv  = []
     binari= bin(N)[2:]
     if binari[-1]=='0':
          return(0)
     else:
          for base in range(2,11):
               i = int(binari,base)
               if i in prime:
                    return(0)
               else:
                    for x in prime:
                         if x>=i:
                              break
                         elif i%x==0:
                              triv.append(x)
                              break
          if len(triv)<9:
               return(0)
          else:
               print(binari,end=' ')
               [print(x,end=' ') for x in triv]
               print()
               return(1)

J  = input()
N,J= [int(x) for x in input().split()]
ces= 0
N  = 2147483649
print('Case #1:')

while ces<J:
     if N not in prime:
          t = check(N)
     N+=1
     ces+=t
