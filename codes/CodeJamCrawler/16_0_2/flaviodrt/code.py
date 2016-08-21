def virar(p, happy):
    for i in range(0, happy):
        p[i] = "+"

def flip(p):
    flip = 0
    panquecas = [i for i in p]
    
    esperado = ["+"]*len(panquecas)
    while esperado != panquecas:
        if "+" in panquecas and "-" in panquecas:
            
            if panquecas.index("-") < panquecas.index("+"):
                anterior = panquecas.index("+")
                happy = len(panquecas[panquecas.index("-"): anterior])
                
            elif "+" not in panquecas[panquecas.index("-"):]:
                happy = len(panquecas)
                
                flip += 1
            else:
                ptemp = panquecas[panquecas.index("-"):]
                happy = panquecas.index("-") + ptemp.index("+") 
                flip += 1
                
            flip += 1
        else:
            happy = len(panquecas)
            flip += 1
        
        virar(panquecas, happy)
        
        
    return flip

def resolver():
    arquivo = open('B-large.in', "r")
    resultado = open('resultado_large.out', "w+")
    
    for i, j in enumerate(arquivo.readlines()):
        if i == 0:
            continue
        
        ps = str(j).strip()
        print "Solving {0}".format(ps)
        flips = flip(ps)
        output = "Case #{0}: {1}\n".format(i, flips)
        #print output
        resultado.write(output)
        
    arquivo.close()
    resultado.close()
