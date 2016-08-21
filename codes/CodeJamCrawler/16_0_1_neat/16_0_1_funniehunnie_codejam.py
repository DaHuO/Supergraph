case = int(input())
for i in range(case):
    num = int(input())
    array = []
    index = 1
    final = "INSOMNIA"
    if num > 0:
        while len(array) < 10:
            final = str(index * num)
            for j in final:
                if j not in array:
                    array.append(j)
            index += 1
    print("Case #%i: %s" %(i + 1, final))
