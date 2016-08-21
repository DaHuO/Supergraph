def flip(b):
    if b == "+":
        return "-"
    if b == "-":
        return "+"


t = int(input())

output = open("output.txt", "w")

for i in range(1, t + 1):
    count = 0
    stack = input()
    s = list(stack)

    for q in range(len(s) - 1, -1, -1):
        if s[q] == "-":
            count += 1
            
            upper = []
            for p in range(len(s[:q+1])):
                upper.append(flip(s[p]))
            s = upper + s[q+1:]
                

        
    output.write("Case #{}: {}\n".format(i, count))

output.close()
