File = str(input("Enter filepath: "))
Out = str(input("Enter fileout: "))
myFile= open(File,"r" )
myLines = list(myFile)
myFile.close()
i = 0

text_file = open(Out,"w")

while i<len(myLines):
	myLines[i] = myLines[i].rstrip('\n')
	myLines[i] = int(myLines[i])
	i = i+1
inp = myLines[0]
i = 0
q = 0
while i<inp:
    usrinp = myLines[q+1]
    inp1 = str(i+1)
    inp1.strip()
    inp1 = "#"+inp1
    if usrinp == 0:
        inpx = str(inp1)
        towrite = ("Case "+inpx+": "+"INSOMNIA")
        print(towrite, file=text_file)
    else:
        n = 0
        p = 1
        usrinp1 = []
        while n==0:
            usrinp2 = usrinp*p
            usrinp1 = usrinp1 + list(map(int, str(usrinp2)))
            usrinp1 = sorted(usrinp1)
            if 1 in usrinp1:
                if 2 in usrinp1:
                    if 3 in usrinp1:
                        if 4 in usrinp1:
                            if 5 in usrinp1:
                                if 6 in usrinp1:
                                    if 7 in usrinp1:
                                        if 8 in usrinp1:
                                            if 9 in usrinp1:
                                                if 0 in usrinp1:
                                                    n = 1
                                                    inpx = str(inp1)
                                                    usrinpx = str(usrinp2)
                                                    towrite = ("Case "+inpx+": "+usrinpx)
                                                    print(towrite, file=text_file)
                                                    
            p = p+1
    q = q+1  
    i = i+1
text_file.close()
