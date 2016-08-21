








#Case: X
X = 1



#Output fil
output = open('output_problem_b_large.txt', 'wb')



#Metode: Skriv ut
def skriv_ut(input_in):

    #Linjen som skal skrives ut
    tmp_linje = 'Case #%d: %s\n' % (X, str(input_in))
    global X
    X += 1


    #Skriver ut linjen til fil
    output.write(bytes(tmp_linje, 'UTF-8'))





#Metode: Finner antall flips som må til
def antall_flips(sekvens_in):

    #Par
    par = []

    #Antall flips
    flips = 0


    #Deler opp sekvensen, et par av gangen
    for i in range(0, len(sekvens_in)-1):
        tmp = str(sekvens_in[i:i+2]).rstrip()
        par.append(tmp)


    #Går gjennom listen 'par'
    extra = 0
    main = False
    for p in par:
        if p == '+-':
            flips += 2
            main = True

        elif p == '-' or p == '--' or p == '-+':
            if not main:
                extra = 1


    #Returnerer antall flips
    return (flips + extra)






#Leser input filen
with open('B-large.in') as fil:

    #Antall testcaser: T
    T = fil.readline()

    #Leser gjennom T-antall N-tall
    for N in fil:
        skriv_ut(antall_flips(N))









#Lukker fil
output.close()
