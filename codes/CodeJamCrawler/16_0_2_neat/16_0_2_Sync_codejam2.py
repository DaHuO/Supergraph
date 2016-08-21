def readFile(filename):
    info = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            info.append(line)
    return info

def pancake(stack):
    sign = stack[0]
    count = 0
    for i in range(1, len(stack)):
        if stack[i] != sign:
            count += 1
            sign = stack[i]
    if stack[-1] == '-':
        count += 1
    return count

def main():
    filename = "data.txt"
    info = readFile(filename)
    for i in range(1, len(info)):
        result = pancake(info[i])
        print ("Case #{0}: {1}".format(i, result))
