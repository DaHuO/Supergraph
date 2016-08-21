f = open("B-large.in", 'r')
cases = f.readline()
lines = f.readlines()
f.close()
case = 1
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
print(lines)

case = 1
for i in lines:
    stack = i
    count = 0
    for i in range(len(stack)):
        now = stack[i]
        if i+1 < len(stack) and stack[i+1] != now:
            count += 1
    if stack[-1] == '-':
        count += 1
    
    out = open("output.txt", 'a')
    out.write("Case #"+str(case)+': '+str(count)+'\n')
    out.close()
    
    case += 1
