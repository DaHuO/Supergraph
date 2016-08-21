from sys import stdin
def main():
  casos = int(stdin.readline().strip())
  ban = False
  for i in range(casos):
    m = stdin.readline().strip()
    cont = 0
    for j in range(0,len(m)):
      if(j+1 < len(m) and m[j]=='-' and m[j+1]=='+'): cont+=1
      elif(j+1 < len(m) and m[j]=='+' and m[j+1]=='-'): cont+=1
      if(j == (len(m)-1) and m[j]=='-'): cont+=1
    print("Case #{0}: {1}".format(i+1,cont))
main()
