def flipPancake(top):
    for i in range(len(top)):
        if top[i] == '-':
            top[i] = '+'
        else:
            top[i] = '-'

    top.reverse()
    return top

n = int(input())
for j in range(1,n+1) :
    minusIndex = 0
    plusIndex = 0
    result = []
    count = 0
    str_ = input()
    list_ = list(str_)
    size = len(list_)
    if list_[0] == '+' and list_[-1] == '-' and len(list_) != 2:
        if list_.count('+') != 1:
            for i in range(len(list_)+1):
                if list_[i] != '+':
                   plusIndex = i-1
                   break

        if plusIndex == 0:
            list_[0] = '-'
            count += 1
        else:
            list_ = flipPancake(list_[:plusIndex+1]) + list_[plusIndex+1:]
            count += 1

    if list_[-1] == '-':
        list_ = flipPancake(list_)
        count += 1

    for i in range(-1,-(len(list_)+1),-1):
        if list_[i] != '+':
            minusIndex = i
            break

    if minusIndex != 0:
        result = list_[minusIndex+1:] + result
        list_ = list_[:minusIndex+1]
    else:
        result = list_ + result
        list_ = []

    while len(list_) != 0:
        minusIndex = 0
        plusIndex = 0
        if list_[-1] == '+':
            for i in range(-1,-(len(list_)+1),-1):
                if list_[i] == '-':
                    minusIndex = i
                    break
            if minusIndex == 0:
                result = list_ + result
                list_ = []
            else:
                result = list_[minusIndex+1:] + result
                list_ = flipPancake(list_[:minusIndex+1])
                count += 1
        else:
            for i in range(-1,-(len(list_)+1),-1):
                if list_[i] == '+':
                    plusIndex = i
                    break
            if plusIndex == 0:
                result = list_ + result
                list_  = []
            else:
                result = list_[plusIndex+1:] + result
                list_ = flipPancake(list_[:plusIndex+1])
                count += 1

    result = ''.join(result)
    if result.count('+') != len(result):
        result = result.replace('-','+')
        count += 1

    print('CASE #',end='')
    print(j,end=': ')
    print(count)



