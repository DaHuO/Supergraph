counter = 0
f = open("output.out", mode='w')
with open("lol.in") as file:
    for y in file:
        counter += 1
        finalstr = ""
        finalstr += y[0]
        for i in range(1,len(y)):
            if ord(y[i]) > ord(finalstr[0]) or ord(y[i]) == ord(finalstr[0]):
                finalstr = y[i] + finalstr
            else:
                finalstr += y[i]
        f.write ("Case #" + str(counter) + ": " + finalstr)
            
f.close()
