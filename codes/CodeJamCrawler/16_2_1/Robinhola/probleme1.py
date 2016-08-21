# encoding: utf-8
import sys
from random import randint
import math

def position (pos, k):
        
    return 1

#Ouverture du fichier
try:
    fo = open("test-practice.in.txt", "r") #r+ a+
    foo = open("test-practice.out.txt", "w") #r+ a+
except:
     print "FAILURE lecture data"
     sys.exit()    


line = fo.readline()
print "la ligne indique : ", line
nb_cases = int(line)

case = 1
while(case <= nb_cases):
    line = fo.readline().rstrip("\n")
    word = line
    solut = "Case #" + str(case) + ": "
    nombre = []


    print word
    
    n = word.count("Z",0, len(word))
    i = 0
    while i < n :
        word = word.replace("Z", "", 1)
        word = word.replace("E", "", 1)
        word = word.replace("R", "", 1)
        word = word.replace("O", "", 1)
        i = i + 1
        nombre.append(0)
        
        
    print word
        
    n = word.count("W",0, len(word))
    i = 0
    while i < n :
        word = word.replace("T", "", 1)
        word = word.replace("W", "", 1)
        word = word.replace("O", "", 1)
        i = i + 1
        nombre.append(2)
        
        
    print word
        
    n = word.count("U",0, len(word))
    i = 0
    while i < n :
        word = word.replace("F", "", 1)
        word = word.replace("O", "", 1)
        word = word.replace("U", "", 1)
        word = word.replace("R", "", 1)
        i = i + 1
        nombre.append(4)
    
    print word
    
    
    n = word.count("F",0, len(word))
    i = 0
    while i < n :
        word = word.replace("F", "", 1)
        word = word.replace("I", "", 1)
        word = word.replace("V", "", 1)
        word = word.replace("E", "", 1)
        i = i + 1
        nombre.append(5)
        
        
    print word
    
        
    n = word.count("X",0, len(word))
    i = 0
    while i < n :
        word = word.replace("S", "", 1)
        word = word.replace("I", "", 1)
        word = word.replace("X", "", 1)
        i = i + 1
        nombre.append(6)
        
    print word
    
        
    n = word.count("O",0, len(word))
    i = 0
    while i < n :
        word = word.replace("O", "", 1)
        word = word.replace("N", "", 1)
        word = word.replace("E", "", 1)
        i = i + 1
        nombre.append(1)
        
    print word
    
        
    n = word.count("R",0, len(word))
    i = 0
    while i < n :
        word = word.replace("T", "", 1)
        word = word.replace("H", "", 1)
        word = word.replace("R", "", 1)
        word = word.replace("E", "", 1)
        word = word.replace("E", "", 1)
        i = i + 1
        nombre.append(3)
        
    print word
        
        
    n = word.count("S",0, len(word))
    i = 0
    while i < n :
        word = word.replace("S", "", 1)
        word = word.replace("E", "", 1)
        word = word.replace("V", "", 1)
        word = word.replace("E", "", 1)
        word = word.replace("N", "", 1)
        i = i + 1
        nombre.append(7)
        
        
    print word
    
        
    n = word.count("G",0, len(word))
    i = 0
    while i < n :
        word = word.replace("H", "", 1)
        word = word.replace("E", "", 1)
        word = word.replace("I", "", 1)
        word = word.replace("G", "", 1)
        word = word.replace("H", "", 1)
        word = word.replace("T", "", 1)
        
        i = i + 1
        nombre.append(8)


    n = word.count("I",0, len(word))
    i = 0
    while i < n :
        word = word.replace("N", "", 1)
        word = word.replace("I", "", 1)
        word = word.replace("N", "", 1)
        word = word.replace("E", "", 1)
        i = i + 1
        nombre.append(9)
        
    nombre.sort()
    print nombre


    i = 0
    
    while i < len(nombre):
        solut = solut + str(nombre[i])
        i = i  + 1
    case = case + 1
    
    print solut
    solut = solut + "\n"
    foo.write(solut)

try:
    fo.close()
    foo.close()
except:
     print "FALLURE fermeture resultat"
     sys.exit()
    
print("fini !")
