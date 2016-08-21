import sys
input = sys.stdin.read().split()[1:]
for case,dat in enumerate(input):
    data = []
    res = 0
    for x in dat:
        k = 0
        if x == '+':
            k = 1
        data.append(k)
    #print(data)
    while sum(data) != len(data):
        res = res + 1
        for index,i in enumerate(data[::-1]):
            if i == 0:
                break
        for i in range(len(data)-index):
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0
    #print(data)
    print("Case #{}: {}".format(case+1, res))
