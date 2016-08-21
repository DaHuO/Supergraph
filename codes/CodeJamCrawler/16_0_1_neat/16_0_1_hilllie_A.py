'''
Created on 10 Apr 2016

@author: David
'''

def readFile():
    with open("A-large.in") as f:
        lines = [int(line) for line in f.readlines()[1:]]
        return lines

results = []
cases = readFile()
for case in cases:
    flag = "INSOMNIA"
    seen = set()
    for i in range(1, 1000):
        #print seen
        #print [int(char) for char in str(case*i)]
        seen.update([int(char) for char in str(case*i)])
        if len(seen)==10:
            flag = case*i
            break
    #exit()
    results.append(flag)

resText = ""
for i, res in enumerate(results):
    resText += "Case #"+str(i+1)+": " + str(res) + "\n"
print resText
with open("res.out", "w") as f:
    f.write(resText)