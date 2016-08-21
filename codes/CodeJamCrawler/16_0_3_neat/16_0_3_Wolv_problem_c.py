




#Bibliotek
from math import sqrt
from itertools import count, islice




#Antall cases
X = 1


#Output fil
output = open('output_problem_b_large.txt', 'wb')



#Metode: Skriv ut
def skriv_ut(N_in, faktorer_in):

    #Skriver ut linjen til fil
    output.write(bytes(str(N_in) + ' ', 'UTF-8'))

    #Skriver ut alle faktorene for N
    for faktor in faktorer_in:
        output.write(bytes(str(faktor) + ' ', 'UTF-8'))

    output.write(bytes('\n', 'UTF-8'))









#Metode: sjekker for primtall
def primtall(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False

        if number == 100001:
            return False

    return True






#Metode: sjekker om det er jamcoin (eventuelt lager en liste)
def jamcoin(N):

    #Liste med N i alle tallsystemene
    N_in_9_bases = [0,0,0,0,0,0,0,0,0]

    #Decimal av N
    N_dec = int(N, 2)

    #Konverterer N til alle tallsystemene
    for base in range(2, 11):

        #Decimal av N i base X
        N_dec_base_x = int(N, base)

        #Sjekker om det konverterte tallet ikke er primtall
        if not primtall(N_dec_base_x):

            N_in_9_bases[base-2] = N_dec_base_x

        #Hvis 'N_dec_base_x' er primtall
        else:
            return None


    #Returnerer listen med N i alle tallsystemene
    return N_in_9_bases






def faktorer(jamcoins_in):

    #Liste over faktorer
    faktorer = []

    #Går gjennom listen 'jamcoins_in'
    for i in range(0, 9):

        #Finner en heltalls-faktor for jamcoinen (int(jamcoins_in[i]**0.5)
        for j in range(3, 20000000, 2):

            #Faktor for jamcoin
            if jamcoins_in[i] % j == 0:
                faktorer.append(j)
                break

            if j == 10001:
                return None


    #Returnerer en liste med faktorer for jamcoinsene
    return faktorer









#Metode: lager en jamcoin
def lag_N(N_in):

    #Cse #1:
    output.write(bytes('Case #1: \n', 'UTF-8'))


    #Antall funnet
    antall = 0

    #Setter sammen en string som skal returneres
    N = '1'

    #Fyller N med 0 og 1
    fyll = 2**(N_in-2)
    for i in range(0, fyll):

        if antall == 500:
            return

        #Lager et binært tall med N digits
        tmp_bin = format(i, '0%db' % (N_in-2))
        N = N + str(tmp_bin) + '1'

        #Kaller metoden 'jamcoin'
        jamcoins = jamcoin(N)

        #Kaller metoden 'faktorer'
        if jamcoins != None:

            liste_faktorer = faktorer(jamcoins)
            if (liste_faktorer != None):
                antall += 1
                skriv_ut(N, liste_faktorer)
                print('Antall: ', antall)
                print(jamcoins)
                print(liste_faktorer)
                print()

        else:
            N = '1'
            continue

        #Nullstiller N
        N = '1'




lag_N(32)




#Lukker fil
output.close()
