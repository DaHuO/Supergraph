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
    line = fo.readline()
    line = line.split()
    n = int(line[0])
    print str(n)
    
    solut = "Case #" + str(case) + ":"
    
    i = 0
    lines= []
    tailles = []
    while(i<2*n - 1):
        lines.append(fo.readline().rstrip("\n"))
        k = 0
        LINE = lines[i].split()
        while(k<len(LINE)):
            tailles.append(int(LINE[k]))
            k = k + 1

        i = i + 1
        
    print tailles
        
    tailles.sort()
    print tailles

    j = 1
    while(j<=2500):
        while(tailles.count(j)!= 0 and tailles.count(j)!= 1):
            tailles.remove(j)
            tailles.remove(j)
        j = j + 1
    
    print tailles
    print lines
    
    i = 0
    tailles.sort()
    while(i<len(tailles)):
        solut = solut + " " + str(tailles[i])
        i = i + 1
    case = case + 1
    
    solut = solut + "\n"
    print solut
    foo.write(solut)

try:
    fo.close()
    foo.close()
except:
     print "FALLURE fermeture resultat"
     sys.exit()
    
print("fini !")