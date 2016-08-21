__author__ = 'Alex'


def checkArray(array):
    for slot in array:
        if slot == False:
            return False
    return True

def algorithm(N):
    if N == 0:
        return 'INSOMNIA'

    allten = False
    arr = [False] * 10
    counter = 1

    while not allten:
        stringN = str(N*counter)
        listN = list(stringN)
        for i in listN:
            arr[int(i)] = True
        allten = checkArray(arr)
        if allten:
            return N*counter
        counter+=1

i = 0
with open("C:/Users/Alex/Downloads/A-large.in","r") as f:
    for line in f:
        if i != 0:
            print('Case #%s: %s'%(i,algorithm(int(line))))
        i+=1

# while i < 1000000:
#     print('Case #%s: %s'%(i,algorithm(int(i))))
#     i+=1


