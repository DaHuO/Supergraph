def openFile(fileName):
    lines = []
    line_number = 0
    with open(fileName, encoding='utf-8') as a_file:
        for a_line in a_file:
            if(line_number!=0):
                lines.append(a_line.rstrip())
            line_number += 1
    return lines


cases = openFile("A-large.in")
#print (cases)
for i in range(0,len(cases)):
    last=0
    if cases[i] != "0":
        #print(i)
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        j=1
        endOfSearch = False
        while endOfSearch == False:
            #print(j)    
            dig=int(cases[i])*j
            strList = list(str(dig))
            #print (strList)
            for k in range(0,len(strList)):
                if strList[k] in digits:
                    #print(strList[k])
                    digits.remove(strList[k])
                    #print(digits)
                    if len(digits)==0:
                        last=dig
                        endOfSearch = True
                        #break
            j=j+1
    if(last)==0:
        value="INSOMNIA"
    else:
        value=str(dig)
    print ("Case #"+str(i+1)+": "+value)
