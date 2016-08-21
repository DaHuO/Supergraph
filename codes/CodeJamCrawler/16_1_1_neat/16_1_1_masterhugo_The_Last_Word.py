from sys import stdin
import collections

cont = 0

def imprimir(lista,cad):
  print("Case #{0}: ".format(cont),end="")
  for i in range(len(lista)):
    print(cad[lista[i]],end="")
  print()

def calcular(cad):
  lista=collections.deque()
  pivot = cad[0]
  lista.append(0)
  for i in range(1,len(cad)):
    if(cad[i]>=pivot):
      pivot=cad[i]
      lista.appendleft(i)
    else:
      lista.append(i)
  imprimir(lista,cad)

def main():
  global cont
  casos = int(stdin.readline().strip())
  cont = 0
  while(casos>cont):
    cont+=1
    cadena = stdin.readline().strip()
    calcular(cadena)
main()
