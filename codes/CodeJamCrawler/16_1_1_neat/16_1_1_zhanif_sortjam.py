
f = open("A-large (1).in")
lines = f.readlines()
out = open("outputALarge.txt", "w")
cases = int(lines.pop(0))

for i in range(cases):
    final = ""
    s = lines.pop(0)
    for char in s:
        if final == "":
            final+=char
        elif char >= final[0]:
            final = char + final
        else:
            final += char
    #print final
    out.write("Case #"+ str(i+1) + ": " + final)

f.close()
out.close()
            
    
    
