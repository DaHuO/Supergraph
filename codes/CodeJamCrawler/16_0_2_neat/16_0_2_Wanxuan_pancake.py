t = int(raw_input()) 
for i in xrange(1, t + 1):
    face = raw_input()
    faceList = [] 
    for f in face:
        faceList.append(f)
    count = 0
    j = 0
    plus = filter(lambda a: faceList[a]=="+", range(0,len(faceList)))
    minus = filter(lambda a: faceList[a]=="-", range(0,len(faceList))) 
    if "-" not in faceList:
        print "Case #{}: {}".format(i, 0) 
    elif "+" not in faceList:
        print "Case #{}: {}".format(i, 1)
    elif faceList == ['-', '+']:
        print "Case #{}: {}".format(i, 1)
    elif faceList == ['+', '-']:
        print "Case #{}: {}".format(i, 2)
    else:
        while "-" in faceList and j < len(faceList):     
            # -++ first time plus
            print j
            if plus != [] and j == plus[0] and j != 0:
                count += 1
                print "1count:"+str(count)
                for n in range(j):
                  faceList[n] = "+" 
                plus = filter(lambda a: faceList[a]=="+", range(0,len(faceList)))
                minus = filter(lambda a: faceList[a]=="-", range(0,len(faceList))) 
                print plus
                print minus
                
            # +-- first time minus
            if j == minus[0] and j != 0:
                count += 1
                print "4count:"+str(count)
                for n in range(j):
                    faceList[n] = "-"  
                plus = filter(lambda a: faceList[a]=="+", range(0,len(faceList)))
                minus = filter(lambda a: faceList[a]=="-", range(0,len(faceList)))                 
                print plus
                print minus 
                           
            # --+ last time minus
            if j == minus[-1]:
                count += 1
                print "2count:"+str(count) 
                for n in range(j):
                  faceList[n] = "+" 
                break 
                
            # ++-  last time plus
            if plus != [] and j == plus[-1]:
                count += 1
                print "3count:"+str(count)
                for n in range(j+1):
                    faceList[n] = "-"  
                plus = filter(lambda a: faceList[a]=="+", range(0,len(faceList)))
                minus = filter(lambda a: faceList[a]=="-", range(0,len(faceList))) 
                print plus
                print minus              
            
     
            j += 1      
        print "Case #{}: {}".format(i, count)
