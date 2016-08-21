def numberOfTimes(case):
    seen_letters = []
    for i in list(str(case)):
        if i not in seen_letters:
            seen_letters.append(i)
    n = 1
    number = n * case
    while len(seen_letters) < 10:
        number = n*case
        n+=1
        for i in list(str(number)):
            if i not in seen_letters:
                seen_letters.append(i)
        if n > 1000:
            return "INSOMNIA"
    return number

dataFile = open("A-large.in")
data = []
for i in dataFile:
    data.append(int(i))
print data

answer = open("googleCodeJamDumpFile.in", 'w')
cases = data[0]
for i in range(1,len(data)): 
    #print i
    #print data[i]
    #print "last number: " + str(numberOfTimes(data[i]))
    answer.write("Case #" + str(i) + ": " + str(numberOfTimes(data[i])))
    if i < len(data) - 1:
        answer.write("\n")