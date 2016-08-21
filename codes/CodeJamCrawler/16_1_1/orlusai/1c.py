import sys
sys.setrecursionlimit(30000)

def recurse(word):
    if len(word)<=1:
        return word
    
    mini = recurse(word[:-1])
    opt1 = mini + word[-1]
    opt2 = word[-1] + mini

    return max(opt1, opt2)

file = open("A-large.in")
file.readline()

outFile = open("1.out", "w")

i = 1
for line in file:
    print("Case #" + str(i) + ": " + recurse(line.rstrip()), file=outFile)
    i += 1

outFile.close()
