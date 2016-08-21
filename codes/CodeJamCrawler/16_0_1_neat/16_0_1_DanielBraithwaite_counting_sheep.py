def countSheep(s):
    i = int(s)
    if i == 0:
        return "INSOMNIA"
    
    numbers = []

    count = 1
    while not (len(numbers) == 10):
        i = count * int(s)

        for c in str(i):
            if c not in numbers:
                numbers.append(c)

        count += 1

    return i

o = open('output.txt', 'w+')
f = open('A-large.in', 'r+')
N = int(f.readline())

for i in range(N):
    s = f.readline()
    
    c = int(s)
    res = countSheep(c)

    o.write("Case #" + str(i + 1) + ": " + str(res) + "\n")

f.close()
o.close()

