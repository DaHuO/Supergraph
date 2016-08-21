inp= open('in2.txt', 'r')

n = int(inp.readline())
num = set()
f = open("output2.txt", "w")

for i in range(n):
    N = int(inp.readline())
    matr = list(map(lambda x: inp.readline().split(" "),range(2*N-1)))
    d = dict()
    answer = []
    for x in matr:
        for y in x:
            if int(y) in d:
                d[int(y)] += 1
            else:
                d.update({int(y):1})
    for x in d:
        if(d[x] % 2 == 1):
            answer.append(x)
    answer.sort()
    ans = ""
    for x in answer:
        ans += str(x) + " "
    f.write("Case #" + str(i+1) + ": " + ans + "\n")
inp.close()
f.close()
