file = open('put.in', 'r')
fil3 = open('put.out', 'w')
t = int(file.readline())


toString = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
toInt = {}

i = 0
for s in toString:
    toInt[s] = i
    i += 1


def count(string, res):
    for chr in string:
        if chr in res:
            res[chr] += 1
        else:
            res[chr] = 1
    return res

final = {}

def process(table, i):
    m = 3000
    for j in range(len(toString[i])):
        try:
            m = min(m, table[toString[i][j]])
        except:
            m = 0
    final[i] = m
    if m:
        for j in range(len(toString[i])):
            table[toString[i][j]] -= m


def decode(string, k):
    global final
    res = count(string, {})

    process(res, 0)
    process(res, 6)
    process(res, 8)
    process(res, 2)
    process(res, 3)
    process(res, 4)
    process(res, 5)
    process(res, 7)
    process(res, 1)
    process(res, 9)
    fil3.write('Case #' + str(k + 1) + ': ')
    for i in range(10):
        if final[i]:
            for j in range(final[i]):
                fil3.write(str(i))
    fil3.write('\n')

for i in range(t):
    decode(file.readline().strip(), i)
