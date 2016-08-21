# encoding: utf-8
import sys
from random import randint
import math


#je prends un nombre
#je verifie s'il est premier pour chaque base
#si oui
    #je trouve un diviseur pour chaque base
#si non je recommence

def position (pos, k, c):
    resultat = pos
    i = 1
    while(i < c):
        resultat = resultat + (pos - 1) * pow(k, i)
        i = i + 1
    return resultat

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

nb_case = 1
while(nb_case <= case):
    line = fo.readline()
    line = line.split()
    k = int(line[0])
    c = int(line[1])
    s = int(line[2])
    print str(k)+ " " + str(c) + " " + str(s)
    
    solut = "Case #" + str(nb_case) + ":"
    
    nb_case = nb_case + 1
    
    if(s < k):
        solut = solut + " IMPOSSIBLE\n"
        foo.write(solut)
        continue
    
    i = 1
    while (i <= k):
        solut = solut + " " + str(position(i,k,c))
        i = i + 1
    solut = solut + "\n"
    foo.write(solut)
    
#Fermeture        
try:
    fo.close()
    foo.close()
except:
     print "FALLURE fermeture resultat"
     sys.exit()
    
print("fini !")
