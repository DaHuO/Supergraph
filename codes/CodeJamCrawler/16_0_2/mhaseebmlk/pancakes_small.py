def flip(pancakes,start,end):
    tempStr = ''
    idx = end
    for i in xrange(start,end+1):
        if pancakes[i]=='-':
            tempStr += '+'
        elif pancakes[i]=='+':
            tempStr += '-'
        idx -= 1
    # print i
    if i<(len(pancakes)-1):
        for i in xrange(i,len(pancakes)-1):
            tempStr += pancakes[i+1]
        return (tempStr)
    return (tempStr)[::-1]

def goal(pancakes):
    p = ''
    for x in xrange(0,len(pancakes)):
        p += '+'
    return p

def serverPancakes(pancakes):
    # print 'Input:',pancakes,'and the goal pancakes are:',(goal(pancakes))
    numFlips = 0
    while pancakes!=(goal(pancakes)):
        if len(pancakes)==1:
            if pancakes=='+':
                # print 'The new pancakes are:',pancakes
                return numFlips
            else:
                # print 'The new pancakes are:',flip(pancakes,0,0)
                numFlips += 1
                return numFlips
        elif (pancakes.startswith('+'))and(pancakes.endswith('-')):
            idx = 0;
            for i in xrange(0,(len(pancakes)-1)):
                if pancakes[i] == '+':
                    idx += 1
                else:
                    break
            pancakes = flip(pancakes,0,(idx-1))
            numFlips += 1
        else:
            i = len(pancakes)-1
            while i>=0:
                if pancakes[i]=='-':
                    pancakes = flip(pancakes,0,i)
                    numFlips += 1
                    # print '------ \nFlipping',pancakes,'between 0 and',i,'\nNew pancakes are:',pancakes,'\n'
                i -= 1
    # print 'Final numFlips=',numFlips,
    # print pancakes,
    return numFlips


if __name__ == '__main__':


    testCases = int(raw_input())
    for x in xrange(0,testCases):
        print 'Case #'+(str(x+1))+':',(serverPancakes(raw_input()))
