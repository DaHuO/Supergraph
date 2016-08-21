def convert(n,liste):
    n=str(n)
    for i in n:
        liste.append(int(i))
    liste=sorted(liste)
    return liste
    

def output1(n):
    a=n    
    liste=[]
    if n==0:
        return("INSOMNIA")
    convert(a,liste)
    while len(liste)<10:
        n=n+a        
        convert(n,liste)
        liste=list(set(liste))
    return str(n)

input=open("A-large.in","r")
T=input.readline()
output=open("output.txt","w")

i=0 
for ligne in input:
    i+=1
    output.write('Case #')
    output.write(str(i))
    output.write(': ')
    output.write(output1(int(ligne)))
    output.write('\n')
    
output.close()