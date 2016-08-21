f = open("B-large.in", 'r')
fo = open("B-large.out", 'w')

t = int(f.readline())

def solve(arr):
    ar0 = [arr[0]]
    for e in arr:
        if ar0[-1] != e:
            ar0.append(e)
    if ar0[-1] == '\n':
        ar0.pop()
    if ar0[-1]== '+':
        return len(ar0)-1
    else:
        return len(ar0)

for i in range(t):
    case = f.readline()
    fo.write("Case #"+str(i+1)+": "+str(solve(case))+'\n')