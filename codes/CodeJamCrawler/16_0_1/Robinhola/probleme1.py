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
    word = []
    word.append(line[0])

    solut = "Case #" + str(case) + ": "
    
    print word
    
    i = 1
    print line
    print len(line)
    while(i<len(line)):
        if (line[i] < word[0]):
            word.append(line[i])
        else:
            word.insert(0,line[i])
        i = i + 1

    
        
    i = 0
    while(i<len(word)):
        solut = solut + word[i]
        i = i + 1

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
