import math, time

def isPrime(n):
    if n == 2:
        return True
    x = 2
    while x <= n**0.5 +1:
    
        if n % x == 0:
            return False
        x +=1
    return True

def fattorizza(n):
    d = 2
    f = []

    if isPrime(n):
        return n
     
    while n > 1:
        
        

        if n % d == 0:
            return d
           
        else:
            if d == 2:
                d = 3
            else:
                d += 2
    return f   

t1 = time.time()    
n= 0
finput = open("Qual_2016_III_sample_input.txt","r")
foutput = open("output.txt","w")
testcase = []
for line in finput:
    if line[:-1] == "\n":
        dati = line[:-1].split()
    else:
        dati = line.split()
    if n == 0:
        T = int(dati[0])
          
    else:
        if n <= T:
           testcase.append(dati[0])
                
    n +=1

N = 16
J = 50
#print (testcase)
txt_output = "Case #1:\n"
trovati = 0
jamcoin ="1"+"0"*(N-2)+"1"
#print (jamcoin)
tentativi = 0

while trovati<J:
    #print (jamcoin," ",end="")

    divisori = ""
    trovato = True
    for n in range(2,11):
        #print (n)
        valore = int(jamcoin[-1])
        for k in range(2,N+1):
            valore = valore + n**(k-1) * int(jamcoin[-k])
        #print ("base",n,"valore:",valore)
        d = fattorizza(valore)
        if d != valore:
            divisori += str(d) + " "
            trovato = True
        else:
            trovato = False
            break
    if trovato:
        trovati +=1
        txt_output = txt_output+ jamcoin +" "+ divisori[:-1] + "\n"
        #print (trovati,jamcoin, divisori)
    #else:
        #print ("")
        
    tentativi +=1
    binario = bin(tentativi)[2:]
    corpo = str(binario)
    jamcoin = "1"+"0"*(N-2-len(corpo))+corpo+"1"
    #print (jamcoin)
    

    
txt_output = txt_output[:-1]   
#print (txt_output)
t2 = time.time()
#print (t2-t1)
foutput.write(txt_output)
foutput.close()
finput.close()
