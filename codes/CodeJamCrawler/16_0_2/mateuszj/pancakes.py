
q = list()
p = list()

def countResult():
    q = [0]*len(p)
    for i in range(len(p)):
        if p[i] == '+':
            q[i] = 1
        else:
            q[i] = 0
    changes = 0
    for i in reversed(range(len(p))):
        if (q[i] + changes) % 2 == 0:
            changes += 1
    return changes

m = int(input())
for l in range(1,m+1):
    p = list(input())
    print("Case #",l,": ",countResult(), sep='')
