
f = open("B-large.in")
fw = open("output.txt", 'w+')

testCases = 0
minManeuver = 0

first_line = f.readline()
testCases = int(first_line)

def flipStringTo(s, toIndex):

    # listStr = list(s)
    #
    # print ('before #{} -- {}\n'.format(listStr, toIndex))
    #
    # for i in xrange(0, toIndex / 2):
    #     listStr[i], listStr[toIndex - i] = listStr[toIndex - i], listStr[i]
    #     pass

    print ('before {} toIndx {}\n'.format(s, toIndex))

    listStr = []

    for i in xrange(0, toIndex):
        listStr.append(s[toIndex - i - 1])
        pass

    for i in xrange(toIndex, len(s)):
        listStr.append(s[i])
        pass

    for i in xrange(0, toIndex):
        if listStr[i] == '-':
            listStr[i] = '+'
        else:
            listStr[i] = '-'
        pass

    print ('after {} toIndx {}\n'.format(''.join(listStr), toIndex))
    return ''.join(listStr)
    pass

for ee in xrange(0, testCases):

    s = f.readline() # S
    bigS = s
    minManeuver = 0

    for i in xrange(0, len(s)):
        if s[i] == '-':
            endOfSadSeries = i
            for j in xrange(i + 1, len(s)):
                if s[j] == '+':
                    endOfSadSeries = j - 1
                    break
                endOfSadSeries = j
                pass
            if i > 0 and s[i - 1] == '+':
                minManeuver += 1
                s = flipStringTo(s, i)
            minManeuver += 1
            s = flipStringTo(s, endOfSadSeries + 1)
        pass

    fw.write('Case #{}: {}\n'.format(ee+1, minManeuver))
    pass

f.close()
fw.close()
