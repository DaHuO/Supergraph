import sys
sys.stdout = open("output.txt", "w+")

def answer(string):
    string += "+"

    result = 0
    for i in range(len(string) - 1):
        result += int(string[i] != string[i + 1])

    return result


for i in range(int(raw_input())):
    print "Case #%d: %s" % (i + 1, answer(raw_input()))
