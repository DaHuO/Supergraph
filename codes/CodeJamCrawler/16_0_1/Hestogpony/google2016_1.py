import datetime

file = open("A-large.in")
outputfile = open("output.out", "w")

n = file.next()

start = datetime.datetime.now()
for i in range(1, int(n) + 1):
    values = [integers for integers in range(0, 10)]
    cur = file.next()
    found = False
    for j in range(1, 100000):
        if len(values) == 0:
            found = True
            outputfile.write("Case #" + str(i) + ": " + str(number) + "\n")
            break
        number = str(int(cur) * j).replace("/n", "")
        chars = list(number)
        for c in chars:
            if int(c) in values:
                values.remove(int(c))
    if not found:
        outputfile.write("Case #" + str(i) + ": INSOMNIA" + "\n")
end = datetime.datetime.now()
print str(end - start)
outputfile.close()

