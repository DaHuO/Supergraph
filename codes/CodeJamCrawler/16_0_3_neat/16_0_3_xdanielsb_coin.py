from __future__ import print_function
import math


entrada = open("in.txt", "r+")
salida = open("out.txt", "r+")
primos = open("primos.txt", "r")
divisorf = open("divisores.txt", "r+")

cases = int(entrada.readline())
listPrimos =[]
soluciones = []
divisores ={}
divisores2 ={}

def is_prime(n): ##Crea una lista de numeros primos
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
#    primos.write(str(n)+ "\n")

def to10(n,b):##numero y base
    result=0
    fin =len(n)-1
    ini= 0
    while(ini<=fin):
        #print(n[ini] +"*"+ str(b) +"^" + str(fin-ini) , end=" ")
        result= result+ int(n[ini])* (b**(fin-ini))
        ini = ini+1
   # print(str(n) +" "+str(b)+ " "+str(result))
    return result

def calcDivisor(num):
    inicio=2
    for i in listPrimos:    
        if num%i==0:
            return i
    return -1
        

def verifique(num): ##Este metodo verifica si sus diferentes representaciones son primos
    aux =""
    for m in range (2,11):
        n= to10(num,m)
        if(n in listPrimos):
            return False
        elif(is_prime(n)):
            return False
        else:
            if(n is not ""):
                aux = aux+ str(n)+" "
    divisores[num]= aux
    return True



for i in range(1, cases+1):
  
    #length,  cantidad= 16,50
    salida.write("Case #"+str(i)+": \n")
    print ("Case #"+str(i))
    length,  cantidad=[ int(y) for y in  entrada.readline().split()]
    ##Carga los primos
    for y in primos.readlines():
        if(int(str(y)[:-1])):
            listPrimos.append(int(str(y)[:-1]))
    for y in divisorf.readlines():
        if(y != ""):
            num, div = y[:-1].split()
            divisores2[num]=div
    #print(divisores2)

    ##Begin
    inicio =2 **(length -1) +1
    fin=2 **(length)
    while(inicio<fin and len(soluciones)< cantidad):
        num = str(bin(inicio)[2:])
        if(num[-1]!="0" and verifique(num) ): ##Descarta los que tengan 0 al final
            soluciones.append(int(num))
        inicio = inicio+1

    ##Ahora agregamos las soluciones
    ##print(divisores)
    for sol in soluciones:
        print(str(sol), end=" ")
        salida.write(str(sol)+ " ")
        for j in divisores[str(sol)][:-1].split():
            if(divisores2.has_key(j)):
                print("("+j+ ","+divisores2[j]+ ")", end=" ")
                salida.write(divisores2[j]+ " ")
            else:  
                nas= calcDivisor(int(j))
                print(str(nas), end=" ")
                salida.write(str(nas)+" ")
        print("")
        salida.write("\n")
    soluciones= []
    divisores={}
