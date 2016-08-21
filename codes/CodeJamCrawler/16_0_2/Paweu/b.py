data = map(list, (open('blg.in', 'r').read().splitlines()))
data = data[1:]


def flip(arr):
    for i in range(len(arr)):
        arr[i] = '-' if arr[i] == '+' else '+'
    return arr
output = ""
for i in range(len(data)):
    j = 0
    while '-' in data[i]:
        j += 1
        for ind in range(len(data[i]) - 1, -1, -1):
            if data[i][ind] == '-':
                idx = ind
                break
        data[i][:idx + 1] = flip(data[i][:idx + 1])
    output += "Case #{}: {}\n".format(i + 1, j)

f = open('blg.out', 'w')
f.write(output)
