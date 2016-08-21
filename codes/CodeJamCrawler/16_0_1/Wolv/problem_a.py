







#Antall siffer som er funnet til nå
siffer = []

#Case: X
X = 1



#Output fil
output = open('output_problem_a_large.txt', 'wb')



#Metode: Skriv ut
def skriv_ut(input_in):

    #Linjen som skal skrives ut
    tmp_linje = 'Case #%d: %s\n' % (X, str(input_in))
    global X
    X += 1


    #Skriver ut linjen til fil
    output.write(bytes(tmp_linje, 'UTF-8'))





#Metode: Dekomponerer et tall
def finn_siffer(tall_in):

    #Multipliserer med i
    for i in range(1, 10000):

        #[INSOMNIA]
        if (i == 9999):
            skriv_ut('INSOMNIA')
            return


        #[A] Sjekker om alle sifferne er funnet
        if (len(siffer) != 10):

            #Konverterer til string
            tall = str(tall_in*i)

            #Går gjennom tallet, siffer for siffer
            for j in range(0, len(tall)):

                #Siffer
                tmp = tall[j:j+1]

                #Sjekker om 'tmp' finnes i listen 'siffer'
                if (tmp not in siffer):

                    #Legger inn sifferet
                    siffer.append(tmp)


        #[B] Hvis alle sifferene er funnet
        else:
            skriv_ut(tall_in*(i-1))
            return








#Leser input filen
with open('A-large.in') as fil:

    #Antall testcaser: T
    T = fil.readline()

    #Leser gjennom T-antall N-tall
    for N in fil:

        finn_siffer(int(N))
        siffer = []








#Lukker fil
output.close()
