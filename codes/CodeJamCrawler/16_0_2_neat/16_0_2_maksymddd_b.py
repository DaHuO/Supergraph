cases = int(raw_input())
counter = 0
def flip_all(arr):
    index = 0
    for i in arr:
        if i == '-':
            arr[index] = '+'
        else:
            arr[index] = '-'
        index += 1
    return arr
while (counter < cases):
    case = list(reversed(raw_input()))
    flips = 0
    length = len(case)
    while '-' in case:
        index = 0
        a = 0
        for i in case:
            if i == '+':
                # remove from array
                del case[index]
                break
            else:
                case = flip_all(case)
                flips += 1
                break
            index += 1

    print "Case #"+str(counter+1)+": {}".format(flips)
    counter += 1
