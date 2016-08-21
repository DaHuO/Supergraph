def flipCake(s):
    global flips
    flips+=1
    sz=len(s)
    bottomUp = s[::-1]
    count = 0
    for i in bottomUp:
        
        if i == "-":
            break
        count+=1
    for k in range(sz-count):
        if s[k] == "+":
            s[k] = "-"
        elif s[k] == "-":
            s[k] = "+"
    return 0

file = open("B-large.in")
with open("output.txt","w") as output:
   
    total = int(file.readline()) +  1
    for i in range(1,total):
        print("case #"+str(i)+"done")
        flips = count = 0
        stack=file.readline()
        jack=list(stack)
        jack.remove('\n')
        if len(jack) < 1:
            output.write("Case #"+ str(i) + ": " + str(flips)+"\n")
            continue
        if jack == ["+"]:
            output.write("Case #" + str(i) + ": " + str(flips)+"\n")
            continue
        if jack == ["-"]:
            output.write("Case #" + str(i) + ": 1"+"\n")
            print("Case #" + str(i) + ": 1")
            continue
        while jack != list(len(jack)*"+"):
            flipCake(jack)

        output.write("Case #"+ str(i) + ": " + str(flips)+"\n")
      
        
file.close()
output.close()
