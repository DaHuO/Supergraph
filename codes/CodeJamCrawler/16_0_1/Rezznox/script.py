resp = ""
with open('A-large.in') as archivo:

    for j, line in enumerate(archivo):
        if(j == 0 ):
            continue
        N = int(line)
        arreglo = [False,False,False,False,False,False,False,False,False,False]

        i = 1
        while i < 100:
            temp = N*i
            estanTodos = True
            for x in str(temp):
                arreglo[int(x)] = True
            for x in arreglo:
                if not x:
                    estanTodos = False
                    continue
            if estanTodos:
                resp += "Case #"+str(j)+": "+str(N*i)+"\r"
                break
            i = i + 1
            if i == 100:
                resp += "Case #"+str(j)+": INSOMNIA\r"
f = open('file-large.out', 'w')
f.write(resp)
f.close()
