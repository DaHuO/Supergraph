# encoding: utf-8
import sys
from random import randint
import math


#je prends un nombre
#je verifie s'il est premier pour chaque base
#si oui
    #je trouve un diviseur pour chaque base
#si non je recommence

def choisir_nombre (liste_de_nombre):
    while(1):
        nombre = randint(limite_b, limite_h)
        #print nombre
        if(nombre % 2 == 0):
            nombre = nombre + 1
        string = str(bin(nombre)).replace("0b","")
        if(liste_de_nombre.count(string) == 0):
            liste_de_nombre.append(string)
            #print string + " " + str(len(string))
            return string
            
def conversion(base, string):
    i = 0
    nombre = 0
    while(i < puissance):
        if(string[i] == '1'):
            nombre = nombre + pow(base, puissance - i - 1)
        i = i + 1
    return nombre
    
    
def test_premier(base, string):
    nombre = conversion(base, string)
    k = 2
    while (k < math.sqrt(nombre) and k < 1000):
        if (nombre % k == 0):
            return k
        else:
            k = k + 1
    return 0

#Ouverture du fichier
try:
    fo = open("test-practice.in.txt", "r") #r+ a+
except:
     print "FAILURE lecture data"
     sys.exit()    
     
try:
    foo = open("test-practice.out.txt", "w") #r+ a+
except:
     print "FAILURE lecture resultat"
     sys.exit() 
    
line = fo.readline()
print "la ligne indique : ", line
case = int(line)
line = fo.readline()
print line
line = line.split()
print line
puissance = int(line[0])
k = int(line[1])
print puissance
print k

limite_b = pow(2,puissance-1) + 1  
limite_h = pow(2,puissance) - 2

print str(limite_b) + " et " + str(limite_h)


solut = "Case #1:\n"
foo.write(solut)

cont = True
i = 0
liste = []
while(i <= k):
    if(cont):
        i = i + 1
        
    rep = []
    cont = True
    base = 2
    
    string = choisir_nombre(liste)                  #je prends un nombre

    while(base <= 10):                              #je verifie s'il est premier pour chaque base
        resultat = test_premier(base, string)
        if(resultat == 0):
            cont = False
            break
        else:
            rep.append(str(resultat)) 
            base = base + 1 
            
    if(cont):
        solut = string
        j = 0
        while j < len(rep):
            solut = solut + " " + rep[j]
            j = j + 1
        solut = solut + "\n"
        print solut
        foo.write(solut)
    print "next " + str(i) + " et k " + str(k)
    
#Fermeture        
try:
    fo.close()
    foo.close()
except:
     print "FALLURE fermeture resultat"
     sys.exit()
    
print("fini !")
