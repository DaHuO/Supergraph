import math, time

t1 = time.time()    
n= 0
finput = open("Qual_2016_II_large_input.txt","r")
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
#print (testcase)
txt_output = ""
for n in range(T):
    stack = testcase[n]
    #print (n+1, " ",stack, end = "  ")
    if stack == "-":
        #print (" 1 mossa\n")
        txt_output = txt_output+"Case #"+str(n+1)+": 1\n"
    else:
        mosse = 0
        
        while not stack == "+"*len(stack):
        
            up = stack[0]
            for j in range(1,len(stack)):
                if stack[j] != up:
                    if up == "+":
                        up = "-"
                    else:
                        up = "+"
                    stack = up*j+stack[j:]
                    mosse +=1
                    break
            if stack == "-"*len(stack):
                stack = "+"*len(stack)
                mosse +=1
            #print (stack, "+"*len(stack))
        #print (mosse,"mosse")
    
        txt_output = txt_output+"Case #"+str(n+1)+": "+str(mosse)+"\n"
        
txt_output = txt_output[:-1]   
print (txt_output)
t2 = time.time()
#print (t2-t1)
foutput.write(txt_output)
foutput.close()
finput.close()
