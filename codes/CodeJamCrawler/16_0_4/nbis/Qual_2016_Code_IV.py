import math, time



t1 = time.time()    
n= 0
finput = open("Qual_2016_IV_small_input.txt","r")
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
           testcase.append(dati)
                
    n +=1


print (testcase)
txt_output = ""

for n in range(T):
    K = int(testcase[n][0])
    C = int(testcase[n][1])
    S = int(testcase[n][2])
    txt_output = txt_output + "Case #"+str(n+1)+": "
    if C == 1:
        if S < K:
            txt_output = txt_output + "IMPOSSIBLE\n"
        else:
            for j in range(S):
                txt_output += str(j+1) + "  "
            txt_output =txt_output[:-1]+"\n"
    else:
        if S < K - 1:
            txt_output + "IMPOSSIBLE\n"
        else:
            for j in range(S):
                txt_output += str(j+1) + "  "
            txt_output = txt_output[:-1] + "\n"

    

    
txt_output = txt_output[:-1]   
print (txt_output)
t2 = time.time()
#print (t2-t1)
foutput.write(txt_output)
foutput.close()
finput.close()
