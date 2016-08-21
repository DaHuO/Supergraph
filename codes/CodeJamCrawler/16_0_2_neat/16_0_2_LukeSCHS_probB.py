#By Luke Baird for Google CodeJam Qualifying round 2016
#problem B - Revenge of the Pancakes

#strategy: start at back of list. when we find a -, flip entire list up to there. Then repeat until we reach the front of the list.

def flipList(mList):
    for x in range(len(mList)):
        if (mList[x] == '+'):
            mList[x] = '-'
        else:
            mList[x] = '+'
    #print(mList)
    return mList

for x in range(int(input())):
    #get the -'s and +'s
    minus = '-'
    plus = '+'
    data = input()
    mList = list(data)
    mList.reverse()
    flips = 0
    while True:
        ran = False
        for z in range(len(mList)):
            if mList[z] == minus:
                ran = True
                #flip entire list starting from z
                xList = mList[(z):]
                yList = mList[:(z)] #front
                #print(xList)
                xList = flipList(xList)
                #print(xList)
                mList = yList + xList
                flips += 1
                break
        if (not ran):
            break
    #reversed
    print('Case #{}: {}'.format(x + 1, flips))