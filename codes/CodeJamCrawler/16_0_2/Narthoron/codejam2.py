def allRight(heap):
    return '-' not in heap

def flip(cake):
    if cake == '+':
        return '-'
    else:
        return '+'

x = input()
for i in range(int(x)):
    pancakesin = input()
    pancakes = [j for j in pancakesin]
    flips = 0
    while not allRight(pancakes):
        flips += 1
        first = pancakes[0]
        stopFlip = False
        for j in range(len(pancakes)):
            if pancakes[j] != first:
                break
            pancakes[j] = flip(pancakes[j])

    print("Case #",i+1,": ",flips, sep='')