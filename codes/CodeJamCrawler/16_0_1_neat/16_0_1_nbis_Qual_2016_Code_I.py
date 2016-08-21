import math, time

t1 = time.time()    
n= 0
finput = open("large_input_Qual_2016_I.txt","r")
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

txt_output = ""
for n in range(T):
    N = testcase[n]
    if N == "0" :
        txt_output = txt_output+"Case #"+str(n+1)+": "+"INSOMNIA\n"
    else:
        k = 2
        digits = set(list(N))
        
        sample = set(list("01234567890"))-digits
        insomnia = False
        while len(sample)>0:
            digits = set(list(str(k*int(N))))
            sample = sample - digits
            #print (k*int(N),sample)
            k+=1
            if k>10000:
                insomnia = True
                break
        if insomnia:
            txt_output = txt_output+"Case #"+str(n+1)+": INSOMNIA"+"\n"
        else:   
            txt_output = txt_output+"Case #"+str(n+1)+": "+str((k-1)*int(N))+"\n"
        
txt_output = txt_output[:-1]   
print (txt_output)
t2 = time.time()
#print (t2-t1)
foutput.write(txt_output)
foutput.close()
finput.close()
