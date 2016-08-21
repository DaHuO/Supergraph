inpt = []

with open("input.txt", "r") as file:
    for line in file:
        a = int(line)
        inpt.append(a)

out = open("output.txt", "w+")

for i in range(1, inpt[0]+1):
    N = inpt[i]
    if N == 0:
        out.write("Case #{}: INSOMNIA\n".format(i))
    else:
        dig = []
        c = N
        while not set(dig) == {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            for d in str(c):
                if d not in dig:
                    dig.append(d)
            c += N
        out.write("Case #{}: {}\n".format(i, int(c-N)))

out.close()
