data = map(int,open('ala.in', 'r').readlines())
data = data[1:]


output = ""
for i in range(len(data)):
    if data[i] != 0:
        result_set = set(str(data[i]))
        j = 1
        while True:
            if len(result_set) == 10:
                break
            j += 1
            result_set.update(str(j * data[i]))
        output += "Case #{}: {}\n".format(i + 1, j * data[i])
    else:
        output += "Case #{}: INSOMNIA\n".format(i + 1)

f = open('ala.out', 'w')
f.write(output)
