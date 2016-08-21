__author__ = 'Owen'

def Evacuation(lar):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sol = ""

    sum = 0
    for i in lar:
        sum += int(i)


    while sum > 0:
        M = lar[0]
        Mi = 0
        N = lar[0]
        Ni = 0
        for i in range(len(lar)):
            if lar[i] > M:
                M = lar[i]
                Mi = i

        if Mi == 0:
            N = lar[1]
            Ni = 1

        for i in range(len(lar)):
            if lar[i] >= N and i != Mi:
                N = lar[i]
                Ni = i

        uns = 0
        for i in lar:
            if i == 1:
                uns += 1

        if N > 2 and (M - N) >= 2:
            sol += alph[Mi]+alph[Mi]+" "
            lar[Mi] -= 2
        elif N > 2 and (M - N) == 1:
            sol += alph[Mi]+" "
            lar[Mi] -= 1
        elif N > 2 and M==N:
            sol += alph[Mi]+alph[Ni]+" "
            lar[Mi] -= 1
            lar[Ni] -= 1
        elif N==2 and M != N:
            sol += alph[Mi]+" "
            lar[Mi] -= 1
        elif N == 2 and M==N:
            sol += alph[Mi]+alph[Ni]+" "
            lar[Mi] -= 1
            lar[Ni] -= 1
        elif N==1 and M != N:
            sol += alph[Mi]+" "
            lar[Mi] -= 1
        elif N == 1 and M==2:
            sol += alph[Mi]+" "
            lar[Mi] -= 1
        elif M == 1 and N == 1 and uns%2 == 0:
            sol += alph[Mi]+alph[Ni]+" "
            lar[Mi] -= 1
            lar[Ni] -= 1
        elif M == 1 and N == 1 and uns%2 == 1:
            sol += alph[Mi]+" "
            lar[Mi] -= 1
        elif M == 1 and N == 0:
            sol += alph[Mi]+" "
            lar[Mi] -= 1


        sum = 0
        for i in lar:
            sum += int(i)

    return sol



f = open("A-large.in", "r")
a = []
for line in f:
    a.append(line)

print a[0]


with open("A-l.txt", "w") as text_file:
    for i in range(int(a[0])):

        s = a[2*i+2].split(" ")
        an = []
        for j in s:
            an.append(int(j))

        text_file.write("Case #%s: %s \n" %(i+1, Evacuation(an)))





