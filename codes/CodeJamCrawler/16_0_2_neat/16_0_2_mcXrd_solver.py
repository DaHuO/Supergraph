from b.pankakes import solve


input = []
with open('B-large.bin') as file:
    first = True
    
    
    for one in file:
        if first:
            first = False
            continue
        
        tone=''
        for o in one:
            if o =='+' or o=='-':
                tone += o
            

        input.append(tone)
result = []



file = open("Output.txt", "w")







case =0
for one in input:
    case += 1
    
    r = solve(one)

    tmp = 'Case #'+str(case)+': '+str(r)+'\n'
    
    file.write(tmp)
    
    
file.close()









    