f = open('input.in', 'r')
output = open('output.out', 'w')
lignes=iter(f.read().splitlines())
nbTests=int(next(lignes))

for numeroTest in range(0,nbTests):
    nombre = int(next(lignes))
    if nombre==0:
        reponse = "INSOMNIA"
    else:
        differentsDigits = set(list(str(nombre)))
        leNombre = nombre
        i = 1
        while len(differentsDigits)<10:
            leNombre = i*nombre
            differentsDigits = set(list(differentsDigits) + list(str(leNombre)))
            i += 1
            if i>1000000:
                break
        reponse=str(leNombre)
    output.write("Case #"+str(numeroTest+1)+": "+reponse)
    if numeroTest<nbTests-1:
        output.write("\n")
    print("Reponse="+reponse)