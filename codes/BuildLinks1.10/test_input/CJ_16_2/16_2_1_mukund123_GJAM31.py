tc=int(raw_input())
for i in range(tc):
    inputt=str(raw_input())
    two=three=four=zero=one=five=six=seven=eight=nine=0
    if "W" in inputt:
        two=inputt.count("W")
        for k in range(two):
            inputt=inputt.replace("W", "",1)
            inputt=inputt.replace("T","",1)
            inputt=inputt.replace("O","",1)
    #print inputt
    if "Z" in inputt:
        zero=inputt.count("Z")
        for k in range(zero):
            inputt=inputt.replace("Z","",1)
            inputt=inputt.replace("E","",1)
            inputt=inputt.replace("R","",1)
            inputt=inputt.replace("O","",1)
    #print inputt
    #print inputt
    if "X" in inputt:
        six=inputt.count("X")
        for k in range(six):
            inputt=inputt.replace("S","",1)
            inputt=inputt.replace("I","",1)
            inputt=inputt.replace("X","",1)
    #print inputt
    if "U" in inputt:
        four=inputt.count("U")
        for k in range(four):
            inputt=inputt.replace("F","",1)
            inputt=inputt.replace("O","",1)
            inputt=inputt.replace("U","",1)
            inputt=inputt.replace("R","",1)
    #print inputt
    if "G" in inputt:
        eight=inputt.count("G")
        for k in range(eight):
            inputt=inputt.replace("E","",1)
            inputt=inputt.replace("I","",1)
            inputt=inputt.replace("G","",1)
            inputt=inputt.replace("H","",1)
            inputt=inputt.replace("T","",1)
    #print inputt
    if "T" in inputt:
        three=inputt.count("T")
        for k in range(three):
            inputt=inputt.replace("T","",1)
            inputt=inputt.replace("H","",1)
            inputt=inputt.replace("R","",1)
            inputt=inputt.replace("E","",1)
            inputt=inputt.replace("E","",1)
    if "S" in inputt:
        seven=inputt.count("S")
        for k in range(seven):
           inputt=inputt.replace("S","",1)
           inputt=inputt.replace("E","",1)
           inputt=inputt.replace("V","",1)
           inputt=inputt.replace("E","",1)
           inputt=inputt.replace("N","",1)
    #print inputt
    if "V" in inputt:
        five=inputt.count("V")
        for k in range(five):
           inputt=inputt.replace("F","",1)
           inputt=inputt.replace("I","",1)
           inputt=inputt.replace("V","",1)
           inputt=inputt.replace("E","",1)
        #print inputt
    if "O" in inputt:
        one=inputt.count("O")
        for k in range(one):
           inputt=inputt.replace("O","",1)
           inputt=inputt.replace("N","",1)
           inputt=inputt.replace("E","",1)
    #print inputt
    if "E" in inputt:
        nine=inputt.count("E")
    strr=""
    for k in range(zero):
        strr+="0"
    for k in range(one):
        strr+="1"
    for k in range(two):
        strr+="2"
    for k in range(three):
        strr+="3"
    for k in range(four):
        strr+="4"
    for k in range(five):
        strr+="5"
    for k in range(six):
        strr+="6"
    for k in range(seven):
        strr+="7"
    for k in range(eight):
         strr+="8"
    for k in range(nine):
         strr+="9"
    print "Case #"+str(i+1)+": "+strr   

         
    
    
    
        
