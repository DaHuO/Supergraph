x = int(input())
for i in range(x):
    inp = input()
    top = "Case #" + str(i+1) + ": "
    neq = 0
    for j in range(len(inp)-1):
        if inp[j] != inp[j+1]:
            neq += 1
    if neq % 2:
        if inp[0] == '+':
            print(top + str(neq+1))
        else:
            print(top + str(neq))
    else:
        if inp[0] == '+':
            print(top + str(neq))
        else:
            print(top + str(neq+1))
            
        
