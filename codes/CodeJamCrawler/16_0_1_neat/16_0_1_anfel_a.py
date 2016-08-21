from sys import stdin
def main():
  n = int(stdin.readline().strip())
  for i in range(n):
      d={}
      a = stdin.readline().strip()
      b = int(a)
      c = b
      cont = 0
      j=2
      if(b == 0):
          print('Case #'+str(i+1)+': INSOMNIA')
          continue
      while cont < 10:
          for x in a:
              if x not in d:
                  cont+=1
                  d[x] = x
          if cont < 10:
            b=c*j
            j+=1
            a=str(b)
      print('Case #'+str(i+1)+': '+str(c*(j-1)))
main()
