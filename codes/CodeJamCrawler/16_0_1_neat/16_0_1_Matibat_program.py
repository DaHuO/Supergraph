#!/usr/bin/env python 
#-*- coding: utf-8 -*-
inFile = "/home/matibat/Descargas/A-large.in"
outFile = "/home/matibat/Escritorio/Google/Counting Sheep/output.out"


def main(entrada_, salida_):
  entrada = read(entrada_)
  salida = ""
  
  Ncasos = int(entrada[0])
  
  for Ncaso in range(1, Ncasos + 1):
    print "Calculando caso #%s" %(Ncaso)
    salida += "Case #%s: %s\n" %(Ncaso, lastNumber(entrada[Ncaso]))
    print "Case #%s: %s" %(Ncaso, lastNumber(entrada[Ncaso]))
    
  write(outFile, salida)



def lastNumber(N):
  if int(N) == 0:
    return "INSOMNIA" ##################################################################################################################
  else:
    Nvistos = [False, False, False, False, False, False, False, False, False, False] # Digitos contados
    Num = N
    Contador = -1 # (1 + Contador) * N
    while not (Nvistos[0] and Nvistos[1] and Nvistos[2] and Nvistos[3] and Nvistos[4] and Nvistos[5] and Nvistos[6] and Nvistos[7] and Nvistos[8] and Nvistos[9]):
      Contador += 1
      Num = (1 + Contador) * int(N) # El número que la obeja va contando
      #print "%s: Número %s" %(Contador, Num)
      
      Digitos = DigiSplit(Num) # Separar en dígitos
      #print "Lista de digitos de %s: %s" %(Num, Digitos)
      for d in Digitos:
        #print d
        Nvistos[d] = True
      
      #print Contador, ": ", Nvistos
    #print "La obeja contó hasta el numero %s" %(Num)
    return Num
      
def DigiSplit(num):
  num = str(num)
  splittedNum = []
  for i in range(0, len(num)):
    #print i, ": ", num[i]
    if num[i] != '' and num[i] != '\n':
      splittedNum.append(int(num[i]))
  #print "Número %s separado en dígitos: %s" %(num, splittedNum)
  return splittedNum

def read(archivo):
  temp = open(archivo, "r")
  retorno = temp.readlines()
  temp.close()
  return retorno

def write(archivo, texto):
  temp = open(archivo, "w")
  temp.write(texto)
  temp.close()
  return 0

if __name__ == "__main__":
  main(inFile, outFile)
