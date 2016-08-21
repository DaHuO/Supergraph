def input(filename):
    lines = open(filename).read().split("\n")
    numCases = int(lines.pop(0))
    linesPerCase = int(len(lines)/numCases)
    return [[lines.pop(0) for b in range(linesPerCase)] for a in range(numCases)]


def output(filename, strings):
    file = open(filename, 'w')
    for a in range(len(strings)):
        print("Case #"+str(a+1)+": "+strings[a]+"\n")
        file.write("Case #"+str(a+1)+": "+strings[a]+"\n")

cases = input("input.txt")

strings = []
for case in cases:
    string = case[0]
    word = ""
    for a in string:
        if len(word) == 0:
            word += a
            continue
        if a >= word[0]:
            word = a + word
        else:
            word += a
    strings.append(word)

output("output.txt", strings)
