def rindex(arr, value):
    try: i = arr[::-1].index(value)
    except: return -1
    return len(arr) - i - 1

def swap(raw):
    cakes = [1 if x == '+' else -1 for x in raw]
    iter = 0
    ri = rindex(cakes, -1)
    while ri != -1:
        cakes = [x * -1 for x in cakes[:ri+1]] + cakes[ri+1:]
        ri = rindex(cakes, -1)
        iter += 1
    return iter


n = int(input())
for i in range(n):
    cakes = str(input())
    answ = swap(cakes)
    print('Case #' + str(i+1) + ': ' + str(answ))