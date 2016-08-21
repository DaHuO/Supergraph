def getfinal(n):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    tracked = []
    seen = []
    i = 1
    cur = n
    contine =True
    while digits!=[]:
        cur = n*i
        if cur in seen:
            return "INSOMNIA"
            break
        seen.append(cur)
        temp = str(cur)
        for char in str(cur):
            if char in digits:
                digits.remove(char)
        i+=1
    if digits == []:
        return str(cur)
        
foo = open("A-large.in")
out = open("output.txt", "wb")
lines = foo.readlines();

numCases = int(lines.pop(0))

case = 1
for line in lines:
    res = getfinal(int(line))
    out.write("CASE #" + str(case) + ": " + res + "\n")
    case+=1
    
foo.close()
out.close()
