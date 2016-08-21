fin = open("A-large.in")
fout = open("output.txt", "w")

lines = []
for line in fin:
    lines.append(line.strip())
lines = lines[1:]
#print(lines)

counter = 0
for word in lines:
    counter += 1
    new = ""
    #print("################")
        
    for letter in word:
        if new == "":
            new = letter
            #print("1")
        elif letter < new[0]:
            #print(letter, new)
            new += letter
            #print("2")
        else:
            new = letter + new
            #print("3")
        #print(new)
    #print(new)
    fout.write("Case #" + str(counter) + ": " + new + "\n")

fin.close()
fout.close()
