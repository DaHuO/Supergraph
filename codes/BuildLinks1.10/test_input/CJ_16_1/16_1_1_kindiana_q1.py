__author__ = 'ben'

lines = [line.rstrip('\n') for line in open('input')][1:]

outFile = open("output", "w")

c = 1
for line in lines:
    w = list(line)
    mid = w[0]
    front = []
    back = []
    del w[0]
    for i in w:
        if len(front):
            if ord(i) >= ord(front[0]):
                front.insert(0, i)
            else:
                back.append(i)
        else:
            if ord(i) >= ord(mid):
                front.insert(0, i)
            else:
                back.append(i)
    outFile.write("Case #" + str(c) + ": " + "".join(front) + mid + "".join(back) + "\n")
    c += 1
