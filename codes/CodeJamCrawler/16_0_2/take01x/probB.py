file = open("./B-large.in")
limit = int(file.readline())
index = 1

def swap(line, start, end):
    tmp = line[start:end + 1]
    tmp.reverse()
    for i in range(len(tmp)):
        if tmp[i] == "+":
            line[start + i] = "-"
        else:
            line[start + i] = "+"

while limit > 0:
    line = list(file.readline())
    count = 0
    while True:
        if "-" not in line:
            break
        count += 1
        mi = line.index("-")
        if "+" in line:
            pi = line.index("+")
            swap(line, 0, max([pi, mi]) - 1)
        else:
            swap(line, 0, len(line))
            pi = -1
    print("Case #%d: %d" % (index, count))
    limit -= 1
    index += 1
