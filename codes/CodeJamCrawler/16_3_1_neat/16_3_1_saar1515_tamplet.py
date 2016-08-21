

def evacuation(lst):
    lst = lst.split(' ')
    lst = list(map(int, lst))

    evac = []
    summ = sum(lst)
    x = 0

    index = 0
    while(sum(lst)>0):
        index = getMaxIndex(lst)
        evac.append(str(index))
        lst[index]-=1
        index = getMaxIndex(lst)
        if(lst[index]>(sum(lst)/2)):
            evac[x] += " "+str(index)
            lst[index]-=1
        x+=1

    return evac


def getMaxIndex(lst):
    max = lst[0]
    index = 0

    for itIndex,item in enumerate(lst):
        if(item>max):
            index = itIndex
            max=item

    return index


def planToString(lst):
    lst2=[]
    string=""

    for item in lst:
        lst2 = item.split(' ')
        for item2 in lst2:
            string+=chr(int(item2)+ ord('A'))
        string+=" "
    return string[:-1]


def readFile(path=r"C:\Users\Saar\Desktop\ap.txt"):
    with open(path,'r') as f:
        lst=f.read().splitlines()
    return lst

if __name__ == '__main__':
    file=readFile(r"C:\Users\Saar\Desktop\A-large.in")
    del file[0]
    newF=[]
    for i in range(int((len(file)/2))):
        newF.append(file[(i*2)+1])
    counter = 1
    for item in newF:
        print("Case #"+str(counter)+": "+str(planToString(evacuation(item))))
        counter+=1