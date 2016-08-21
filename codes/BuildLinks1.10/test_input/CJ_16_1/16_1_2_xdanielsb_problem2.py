from __future__ import print_function
import itertools


intxt = open("in.txt", "r")
outtxt = open("out.txt", "r+")

numDeCasos = int(intxt.readline())
lista= []
for i in range (1, numDeCasos+1):
    val = int(intxt.readline())
    print(val)
    listafinal =[]
    listaresultado =[]
    lst2 =[]
    word= []
    lista=[]

    for j in range(1,2*val):
        word =(intxt.readline()[:-1]).split()
        #print(word)
        lista += word
    listafinal=[int (y) for y in lista]
    listafinal.sort()
    print(listafinal)
    for ele in listafinal:
        if(listafinal.count(ele)%2==1):
            listaresultado.append(ele)
    #print(listaresultado)
    [lst2.append(key) for key in listaresultado if key not in lst2]
    outtxt.write("Case #"+str(i)+": ")
    for i in lst2:
        #print(i, end=" ")
        outtxt.write(str(i)+" ")
    outtxt.write("\n")
