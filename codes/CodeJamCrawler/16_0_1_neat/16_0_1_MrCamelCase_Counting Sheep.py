inp  = open("Q1IN.txt").readlines()
out = open("Q1OUT.txt","w")
limit = int(inp[0].rstrip())
qn = 0
for i in inp[1::]:
    qn+=1
    num = int(i.rstrip())
    #print(num)
    if num == 0:
        answer = "INSOMNIA"
    else:
        number = []
        a = set(["0","1","2",'3','4','5','6','7','8','9'])
        counter = 0 
        while set(number)!= a:
            counter += num
            #print(counter)
            for bit in str(counter):
                number.append(bit)
            #print(set(number))
            #print('\n')
        answer = counter
    out.write("Case #%s: %s"%(str(qn),str(answer)))
    #print('\n \n')
    if qn!=limit:
        out.write("\n")

out.close()
#print("Done")
