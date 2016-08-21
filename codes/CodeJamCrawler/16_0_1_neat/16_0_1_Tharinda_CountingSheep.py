t = input()

for i in range(0, t) :
    n = input()
    if n == 0 :
        print "Case #" +str(i+1) + ": INSOMNIA"
        continue
    list = []
    for j in range(0, 10) :
        list.append(j)
    #print list
    end = True
    count = 1
    sum = 1
    while end :
        if(len(list) == 0) :
            break
        sum = n * count
        count +=1
        removeList = []
        for k in range(0, len(list)) :
            if str(list[k]) in str(sum) :
                removeList.append(list[k])
        for l in range(0, len(removeList)) :
            list.remove(removeList[l])
    print "Case #" + str(i+1) + ":", sum