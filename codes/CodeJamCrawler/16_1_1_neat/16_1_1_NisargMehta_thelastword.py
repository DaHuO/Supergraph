tc = int(input())
for t in range(tc):
    s = input()
    output = ""
    for char in s:
        if(output == ""):
            output += char
        elif(char >= output[0]):
            output = char + output
        else:
            output += char
    print("Case #"+str(t+1)+": "+output.upper())
