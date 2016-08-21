#!/usr/bin/env python 
#-*- coding: utf-8 -*-
inFile = "/home/matibat/Descargas/B-large.in"
outFile = "/home/matibat/Escritorio/Google/Revenge of the Pancakes/output.out"

def main(entrada_, salida_):
  entrada = read(entrada_) # Leer texto
  salida = "" # Salida
  
  global Ngiros # Numero de vueltas a darle a los panqueques por caso
  
  #print entrada
  
  Ncasos = int(entrada[0]) # Número de casos
  Ngiros = 0
  
  for Ncaso in range(1, (Ncasos + 1)): # Resolver cada caso
    panqueques = entrada[Ncaso].strip() # Leer los panqueques en el caso Ncaso
    aux = panqueques[0] # Variable auxiliar
    for pos in range(1, len(panqueques)): # Ver cada panqueque
      if aux != panqueques[pos]:                 # Comparar el panqueque con el auxiliar,
        panqueques = negar(panqueques, pos - 1)  # si no están igual girar todos antes del diferente
      aux = panqueques[0]
    if panqueques[0] == "-":
      negar(panqueques, len(panqueques) - 1)
    salida += "Case #%s: %s\n" %(Ncaso, Ngiros)
    Ngiros = 0
  write(outFile, salida)
  
  Ngiros += 1
  return panqueques
  
def negar(cadena, posicion):
  global Ngiros
  
  auxiliar = ""
  for indice in range(0, (posicion + 1)):
    if cadena[indice] == "+":
      auxiliar += "-"
    else:
      auxiliar += "+"
  auxiliar += cadena[(posicion + 1):]
  Ngiros += 1
  return auxiliar
  
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
