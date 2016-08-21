def odcitaj(d, cislo, kolko):
    for c in cislo:
        d[c] -= kolko
    return d

T = int(input())
for tid in range(1, T+1):
    s = input()
    d = {}
    abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in abeceda:
        d[c] = 0
    for c in s:
        if (c in d):
            d[c] += 1
        else:
            d[c] = 1
    vysledok = {}

    vysledok[0] = d['Z']
    d = odcitaj(d, 'ZERO', d['Z'])
    #print(d)
    #print(vysledok)

    vysledok[2] = d['W']
    d = odcitaj(d, 'TWO', d['W'])
    #print(d)
    #print(vysledok)

    vysledok[4] = d['U']
    d = odcitaj(d, 'FOUR', d['U'])
    #print(d)
    #print(vysledok)

    vysledok[6] = d['X']
    d = odcitaj(d, 'SIX', d['X'])
    #print(d)
    #print(vysledok)

    vysledok[8] = d['G']
    d = odcitaj(d, 'EIGHT', d['G'])
    #print(d)
    #print(vysledok)

    vysledok[7] = d['S']
    d = odcitaj(d, 'SEVEN', d['S'])
    #print(d)
    #print(vysledok)

    vysledok[5] = d['F']
    d = odcitaj(d, 'FIVE', d['F'])
    #print(d)
    #print(vysledok)

    vysledok[3] = d['R']
    d = odcitaj(d, 'THREE', d['R'])
    #print(d)
    #print(vysledok)

    vysledok[1] = d['O']
    d = odcitaj(d, 'ONE', d['O'])
    #print(d)
    #print(vysledok)

    vysledok[9] = d['I']
    d = odcitaj(d, 'NINE', d['I'])
    #print(d)
    #print(vysledok)
    v = ''
    for i in range(0, 10):
        for j in range(0, vysledok[i]):
                v += str(i)


    print('Case #{}: {}'.format(tid,str(v)))
