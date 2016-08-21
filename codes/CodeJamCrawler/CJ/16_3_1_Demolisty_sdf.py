
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for O in range(int(input())):
    result = []
    parties = []
    s = 0
    q = input()
    z = input().split()
    parties = [int(i) for i in z]
    while (sum(parties)> 0):
        toRemove = ""
        for p in range(0,2):
            m = max(parties)
            k = [i for i, j in enumerate(parties) if j == m]
            if (m > 1):
                parties[k[0]] -= 1
                toRemove += alphabets[k[0]]
            elif (m == 1):
                if (sum(parties) > 2):
                    parties[k[len(k)-1]] -= 1
                    toRemove += alphabets[k[len(k)-1]]
                elif (sum(parties) == 2):
                    if(len(toRemove) == 0):
                        for b in range(len(k)):
                            parties[k[len(k)-(b+1)]] -= 1
                            toRemove += alphabets[k[len(k)-(b+1)]]
        result.insert(s,toRemove)
        s += 1
    print ("Case #{0}: {1}".format(O+1," ".join(result)))
