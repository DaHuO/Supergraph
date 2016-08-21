x = int(input())
lista = ""
for i in range(0,x):
    y = input()
    k = 1
    b = True
    aux = 0
    while b and y!='0':
        aux = aux + int(y)
        m = str(aux)
        for j in range(0,len(m)):
            if lista.find(m[j]) == -1:
                lista = lista + m[j]
        if(len(lista)== 10):
            print('Case #'+str(i+1)+':', aux)
            b = False
        k = k + 1
    lista = ""
    if y == '0':
        print('Case #'+str(i+1)+': INSOMNIA')