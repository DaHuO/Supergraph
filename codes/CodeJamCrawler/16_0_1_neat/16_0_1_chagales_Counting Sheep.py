def calcula(number):
    auxiliar=0
    resto=0
    div=0
    escape=0
    i=0
    suma=0
    marca=[0,0,0,0,0,0,0,0,0,0]
    while escape==0:
        auxiliar= int(number)*(i+1)
        i=i+1
        div=auxiliar        
        while (div>0):
            resto=div%10
            div=div/10
            for j in range(len(mbase)):
                if(resto==mbase[j]):
                    if(marca[j]==0):
                        marca[j]=1
                        suma=suma+1
        if(suma==10):
            calculo=auxiliar
            escape=1
    return calculo

def sleep(case, number):
    print('Case #'+str(case)+': '+str(number))
    numero=int(number)
    noall=0
    out="nada"
    aux=0
    numint=0
    i=0
    suma=0
    got=0
    marca=[0,0,0,0,0,0,0,0,0,0]
    while noall==0:
        if(int(numero)==0):
            out="INSOMNIA"
            noall=1
            got=1
        elif(numero>999999999):
            numint=int(number)
            for n in range(10):
                aux=numint%10
                numint=numint/10
                for j in range(len(mbase)):
                    if(aux==mbase[j]):
                        marca[j]=1
                        suma=suma+1
                        
            if(suma==10):
                out=number
                noall=1
                got=1
        if(got==0):
            out= calcula(number)
            got=1
            noall=1        
    print("Numero "+str(out))
    outfile = open('OutputCountingSheep.txt', 'a') # Indicamos el valor 'w'.
    outfile.write('Case #'+str(case)+ ': ')
    outfile.write(str(out))
    outfile.write('\n')
    outfile.close()
             
                

mbase=[0,1,2,3,4,5,6,7,8,9]
marca=[0,0,0,0,0,0,0,0,0,0]


print 'Inicio'


f= open('A-large.in','r')
print f
indexCase=0
for line in f:
    print line
    if (indexCase==0):
        cases = line
        indexCase +=1
        print ('Cases ' + str(cases))        
    else:
        sleep(indexCase,line)
        indexCase+=1
