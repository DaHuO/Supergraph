# encoding: utf-8
import sys

def solution(string):
        # on enlève tous les plus à la fin
        while (string.endswith("+")):
            string = string[0:len(string)-1]
        while ("++" in string):
            string = string.replace("++","+")
        while ("--" in string):
            string = string.replace("--","-")
        return len(string)
    
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
k = int(line)

i = 1
while(i <= k):
    line = fo.readline().rstrip()
    solut = "Case #" + str(i) + ": " + str(solution(line)) + "\n"
    foo.write(solut)
    i = i + 1
    
    
#Fermeture        
try:
    fo.close()
    foo.close()
except:
     print "FALLURE fermeture resultat"
     sys.exit()
    
print("fini !")
