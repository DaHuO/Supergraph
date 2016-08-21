from math import sqrt
from itertools import count,islice
import itertools
#input file
file = open("input.txt",'rb')
cases = file.readline()
w_file = open("output2.txt",'wb')
def isPrime(n):
    return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def factors(n):    
        return set(reduce(list.__add__, 
                            ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
for line in file:
    split_line = line.split(" ")
    poss = split_line[0]
    cased = split_line[1]
    print cased
    d = 1
    if(d>cased):
        break
    x = ["".join(seq) for seq in itertools.product("01",repeat = int(poss))]

    w_file.write("Case #" + str(str(d) + ":"  + "\n")) 
    for i in x:
         print d
         if(d>int(cased)):
             break
         if str(i)[0] == '1' and str(i)[len(i) -1] == '1' and isPrime(int(i,2))  == False and isPrime(int(i,3)) == False and isPrime(int(i,4)) == False and isPrime(int(i,5)) == False and isPrime(int(i,6)) == False and isPrime(int(i,7)) == False and isPrime(int(i,8)) == False and isPrime(int(i,9)) == False and isPrime(float(i)) == False :           
               print i
               #get non trvial divisor
               int_i = int(i)
               jj = 0
               cont = 2
               #take any divisor
               divsor_1 = factors(int(i,2)).pop()
               div2 = factors(int(i,3)).pop()
               div3 = factors(int(i,4)).pop()
               div4 = factors(int(i,5)).pop()
               div5 = factors(int(i,6)).pop()
               div6 = factors(int(i,7)).pop()
               div7 = factors(int(i,8)).pop()
               div8 = factors(int(i,9)).pop()
               div9 = factors(int(i)).pop()

               #while(jj == 0):
                #   if divsor % cont == 0:
                 #      jj = count
                  #     print j
                   #    cont +=1
                
               w_file.write(str(i) + " " + str(divsor_1) + " " + str(div2) + " " + str(div3) + " " + str(div4) + " " + str(div5) + " " + str(div6) + " " + str(div7) + " " + str(div8) + " " + str(div9) + "\n") 
               d += 1

               
