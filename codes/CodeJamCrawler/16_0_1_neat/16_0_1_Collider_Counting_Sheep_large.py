in_file = open("A-large.in","r")
T = in_file.readline()
T = int(T)
out_file = open("out_large.out","w")


for i in range(T):
    #print("Case #:",i+1)
    N = in_file.readline()
    Test = [0,0,0,0,0,0,0,0,0,0]
    Check = [1,1,1,1,1,1,1,1,1,1]
    Ok = False
    answer = N
    count = 1
    N = int(N)
    N = str(N)
    MultN = N
    N = int(N)

    if N == 0:
        Ok = True
        answer = "INSOMNIA"

        
    
    while Ok == False:
        for t in MultN:
                c = int(t)
                Test[c] = 1
        if Test == Check:
            Ok = True
            answer = MultN
        
        count = count + 1
        MultN = str(count*N)


    #print(count)
    #print(answer)
    
    out_file.write("Case #"+str(i+1)+": "+answer+"\n")
    #print(N)

in_file.close()
out_file.close()
