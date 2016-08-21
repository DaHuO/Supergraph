def isCorrect(s):
    for char in s:
        if char!= '+':
            return False
    return True

def flip(s):
    res =""
    for char in s:
        if char == "+":
            res+="-"
        elif char=="-":
            res+="+"
    
    return res

def minFlips(s):
    numFlips = 0
    for i in range(len(s)-1, -1, -1):
        if isCorrect(s):
            break
        if(s[i] != '+'):
            pre = flip(s[:i+1])
            post = s[i+1:]
            s= pre+post
            numFlips+=1
            
    return numFlips

f = open("B-large.in")
out = open("outputB.txt", "wb")
lines = f.readlines()

numCases = int(lines.pop(0))

case = 1
for line in lines:
    out.write("Case #" + str(case) + ": " + str(minFlips(line.strip())) + "\n")
    case+=1

out.close()
f.close()
