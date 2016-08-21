file = open("B-large.in", "r")
newFile = open("output.txt", "w")

def CountPancakeFlips(s:str):
    count = 0
    while ("-" in s):
        if ("+" not in s):
            return count+1
        for i in range(len(s)):
            if (s[0] != s[i]):
                s = (("+" * (i+1)) if (s[0] == "-") else ("-" * (i+1))) + s[i+1:]
                break
        count += 1
    return count

testCases = int(file.readline())
for i in range(testCases):
    s = "Case #{}: {}".format(i + 1, CountPancakeFlips(file.readline()))
    if (not i == testCases - 1):
        s += "\n"
    newFile.write(s)

file.close()
newFile.close()
