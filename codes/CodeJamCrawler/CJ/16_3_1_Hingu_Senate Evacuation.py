import string
def main():
    parties = list(string.ascii_uppercase)
    for t in xrange(int(raw_input().strip())):
        n = int(raw_input().strip())
        senators = map(int, raw_input().strip().split(' '))
        output = []; newO = []
        
        while sum(senators) != 0:
            maxValue = max(senators)
            maxIndex = [i for i, j in enumerate(senators) if j == maxValue]
            if len(maxIndex) % 2 == 0:
                for i in xrange(0, len(maxIndex)-1, 2):
                    output.append(parties[maxIndex[i]]+parties[maxIndex[i+1]])
                    senators[maxIndex[i]] -= 1
                    senators[maxIndex[i+1]] -= 1
            else:
                output.append(parties[maxIndex[0]])
                senators[maxIndex[0]] -= 1
                for i in xrange(1, len(maxIndex)-1, 2):
                    output.append(parties[maxIndex[i]]+parties[maxIndex[i+1]])
                    senators[maxIndex[i]] -= 1
                    senators[maxIndex[i+1]] -= 1
        i = 0
        while i < len(output):
            if len(output[i]) == 1 and len(output[i+1]) == 1:
                newO.append(output[i]+output[i+1])
                i += 1
            else:
                newO.append(output[i])
            i += 1
        print 'Case #'+str(t+1)+':', 
        for i in newO:
            print i,
        print

if __name__ == '__main__': 
    main()
