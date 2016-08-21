def isMean(z):
    x = sum(z)
    x = x + 0.0
    for i in range(len(z)):
        if(z[i]>0):
            if(z[i]/x>.5):
                return 1
    return 0
def evacPlan(z):
    result1 = ''
    result2 = []
    for k in range(sum(z)):
        result1 = ''
        result = []
        a = max(z)
        if(a>0):
            i = z.index(a)
            z[i] = z[i] - 1
            result.append(chr(i + ord('A')))
        a = max(z)
        if(a>0):
            i = z.index(a)
            z[i] = z[i] - 1
            if(isMean(z) or z[i]==0):
                if (sum(z)==0):
                    result.append(chr(i + ord('A')))
                else:
                    z[i] = z[i] + 1
            else:
                result.append(chr(i + ord('A')))
        result1 = result1.join(map(str, result))
        result2.append(result1)
        if sum(z)==0:
            break
    return result2

t = input()
for i in range(t):
    n = input()
    for j in range(1):
        z =  map(int,raw_input().split())
        result = evacPlan(z)
        print "CASE #" + str(i+1) + ":" + " " + ' '.join(map(str, result))
