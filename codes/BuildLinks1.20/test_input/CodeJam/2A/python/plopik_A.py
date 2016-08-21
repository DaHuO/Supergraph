t = int(input())

def fusion(a, b):
    c = a + b
    d = b + a
    if(c < d):
        return c
    return d
def mergeSort(name, depth):
    if(depth == 0):
        return name
    else:
        if(name == 'R'):
            other = 'S'
        if(name == 'S'):
            other = 'P'
        if(name == 'P'):
            other = 'R'
        return fusion(mergeSort(name, depth-1), mergeSort(other, depth-1))

def testTree(tree, r, p, s):
    count = [r, p, s]
    for a in tree:
        if(a == 'R'):
            count[0] -= 1
        if(a == 'P'):
            count[1] -= 1
        if(a == 'S'):
            count[2] -= 1
    possibru = True
    for d in count:
        if(d!=0):
            possibru = False
            break
    if(possibru):
        print(tree)
    return possibru
    
for x in range(t):
    print("Case #%d:"%(x+1), end = " ")
    n, r, p, s = map(int, input().split(" "))
    ye = testTree(mergeSort('S', n), r, p, s)
    if(ye):
        continue
    ye = testTree(mergeSort('P', n), r, p, s)
    if(ye):
        continue
    ye = testTree(mergeSort('R', n), r, p, s)

    if(ye):
        continue
    print("IMPOSSIBLE")
