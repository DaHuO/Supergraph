def findMissing(RankList):
    resultList = {}
    for i in xrange(1, 2501):
    
        resultList[str(i)] = 0
        
    for List in RankList:
        
        for ele in List:
            
            resultList[str(ele)] += 1
    result = []
    
    for ele in resultList:
        if resultList[ele] % 2 == 1:
            result.append(int(ele))
    result = sorted(result)
    strresult = ""
    for ele in result:
        if len(strresult) != 0:
            strresult += ' '
        strresult += str(ele)
    return strresult
    

f = open("B-large(2).in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = int(f.readline())
    RankList = []
    for i in xrange(0,2* readline - 1):
        RankList.append(f.readline().strip().split(' '))
    print "Case #" + str(x+1) + ": " + findMissing(RankList)
