from __future__ import print_function
entrada = open("in.txt", "r+")
salida = open("out.txt", "r+")

cases = int(entrada.readline())

for i in range(1, cases+1):
    inicial = [0,1,2,3,4,5,6,7,8,9]
    cont= 2
    original =entrada.readline()
    aux= int(original)
    num =  [int (y) for y in  list((original[:-1]))]
    #print (aux)
    while(len(inicial)>0   and cont<1000000):

        #print (inicial)
        for n in num:
            if (n in inicial):
                inicial.pop(inicial.index(n))
        aux= int(original)*cont
        num = [int (y) for y in str(aux)]
        cont = cont +1
        #print (aux, end=" ")


    if(cont==1000000):
        #print("Case #"+str(i) +": INSOMNIA")
        salida.write("Case #"+str(i) +": INSOMNIA\n")
    else:
        #print("Case #"+str(i) +": "+str(int(original)*(cont-2)))
        salida.write("Case #"+str(i) +": "+str(int(original)*(cont-2))+"\n")
