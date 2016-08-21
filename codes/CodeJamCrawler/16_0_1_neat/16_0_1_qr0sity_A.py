def cycle(number):
    number = abs(number)
    start = number
    obj = set(list(str(1234567890)))
    nochange = 0
    nochange_thresh = 20
    currset, startset = set(list(str(number))), set(list(str(number)))
    while True:
        currset.update(list(str(number)))
        if currset == startset:
            nochange += 1
        if nochange == nochange_thresh:
            return 'INSOMNIA'
        if currset == obj:
            return number
        number += start

n = int(input())
for i in range(n):
    num = int(input())
    answ = cycle(num)
    print('Case #' + str(i+1) + ': ' + str(answ))