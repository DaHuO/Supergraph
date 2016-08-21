T = int(raw_input())

for tc in xrange(T):
    parties =int(raw_input())
    partyNum = [int(x) for x in raw_input().split()]
    evac = 0
    evas = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    aliveparty = parties
    while max(partyNum) != 1 or aliveparty > 2:
            maxy = max(partyNum)
            evas += abc[partyNum.index(maxy)]
            evac += 1
            partyNum[partyNum.index(maxy)] -= 1
            if evac == 2:
                evac = 0
                evas += " "
            aliveparty = 0
            for i in xrange(parties):
                if partyNum[i] != 0:
                    aliveparty += 1
    if evas !="" and evas[len(evas) - 1] != " ":
        evas += " "
    maxy = max(partyNum)
    evas += abc[partyNum.index(maxy)]
    partyNum[partyNum.index(maxy)] -= 1
    evas += abc[partyNum.index(maxy)]
                
    print "Case #" + str(tc + 1) + ": " + evas
                    
               
    
