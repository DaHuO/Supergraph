
T = int(input())
f = open('workfile', 'w')
for j in range(1, T + 1):
    n = int(input())
    hash = {}
    for i in range(0, 2*n - 1):
        array = map(int, raw_input().split())
        for each in array:
            if each in hash:
                hash[each] += 1
            else:
                hash[each] = 1
    answer = []
    string = ""

    for each in hash.keys():
        if hash[each] % 2 == 1:
            answer.append(each)
    answer.sort()
    for each in answer:
        string += "%s " % each

    if len(answer) != n:
        print(hash)
    f.write("Case #%s: %s\n" % (j, string[:-1]))