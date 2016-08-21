from a.bleatrix import solve


input = []
with open('A-large.bin') as file:
    first = True
    
    
    for one in file:
        if first:
            first = False
            continue
        
        input.append(one)
        

result = []




file = open("Output.txt", "w")







case =0
for one in input:
    case += 1
    
    r = solve(int(one))

    tmp = 'Case #'+str(case)+': '+str(r)+'\n'
    
    file.write(tmp)
    
    
file.close()










    