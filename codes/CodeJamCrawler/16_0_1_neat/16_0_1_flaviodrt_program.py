arquivo = open('A-large.in', "r")
resultado = open('resultado_p.out', "w+")
for i, j in enumerate(arquivo.readlines()):
    
    N = int(j)
    
    if i == 0:
        continue 
    
    tracked = []
    
    for t in range(1,201):
        if N == 0:
            output ="INSOMNIA"
            break 
        
        output = t*N
        tracked.append(list(str(output)))
        
        check = list(set(sum(tracked, [])))
        check.sort()
        if check == ok:
            break

    f = "Case #{0}: {1}\n".format(i, output)    
    resultado.write(f)
    print f
    
resultado.close()
arquivo.close()
