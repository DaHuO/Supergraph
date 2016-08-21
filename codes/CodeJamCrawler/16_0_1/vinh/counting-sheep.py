def f(n):
    if n * 2 == n:
        return "INSOMNIA"
    else:
        lookup = set()
        n_str = str(n)
        i = 1

        while len(lookup) != 10:
            intermediate = n * i
            n_str = str(intermediate)
            for j in n_str:
                lookup.add(j)
            i = i + 1
        return intermediate

with open("A-large.in", "r") as ins:
    array = []
    for line in ins:
        array.append(int(line))
last = open('result.txt', 'w')
for i in range(1, len(array)):
    result = str(f(array[i]))
    last.write("CASE #" + str(i)+ ": " + result + "\n")
last.close()