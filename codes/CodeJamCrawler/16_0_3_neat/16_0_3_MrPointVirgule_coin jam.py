from sympy.ntheory.factor_ import smoothness

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + numerals[num % b])

def largest_prime_factor(n):
    p, g = smoothness(n)
    return p


t = int(input())
for k in range(1, t + 1):
    print("Case #" + str(k) + ":")
    taille, nombre = input().split()
    taille=int(taille)
    nombre=int(nombre)
    init = pow(2, taille - 1)-1
    for i in range(0, nombre):
        ok=False
        nbstr=""
        primes = [0]*12
        alla=[0]*12
        while not ok:
            init += 2
            nbstr = baseN(init, 2)
            ok=True
            for b in range(2,11):
                nb=int(nbstr,b)
                alla[b]=nb
                primes[b] = largest_prime_factor(int(nbstr, b))
                if nb==primes[b]:
                    ok=False
                    break

        print(nbstr,end="")
        for j in range(2,11):
            print(" "+str(primes[j]), end="")
        print(flush=True)
