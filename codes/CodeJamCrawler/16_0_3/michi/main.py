
class Coinjam:

    def __init__(self,s):
        self.s = s
        self.factores = []
        self.convertido = 0

    def to_base(self,base):
        res = 0
        cifra = 1
        for c in xrange(len(self.s)-1,-1,-1):
            res = res + int(self.s[c]) * cifra
            cifra = cifra * base
        self.convertido = res    
        #print self.convertido

    def get_factor(self):
        if self.convertido % 2 == 0:
            return 2
        divisor = 3
        while divisor < self.convertido/2:
            if self.convertido % divisor == 0:
                return divisor
            # Heuristica. Hay mas estrellas en el cielo
            if divisor > 50:
                #print "paso"
                return False
            divisor = divisor + 2
        return False    

    def es_coinjam(self):
        for base in xrange(2,11):
            self.to_base(base)
            factor = self.get_factor()
            if not factor:
                return False
            else:
                self.factores.append(factor)

        return True

    def inc(self):
        self.to_base(2)
        next_dec = self.convertido  + 2
        next_str = bin(next_dec)
        self.__init__(next_str[2:])


entrada = open('large.in','r')
salida = open('large.out','w')

T = int(entrada.readline().rstrip('\n'))
NJ = map(int,entrada.readline().strip('\n').split(' '))
N = NJ[0]
J = NJ[1]


s = '1' + '0'*(N-2) + '1'
coin = Coinjam(s)

salida.write("Case #1:\n")
while J>0:
    if coin.es_coinjam():
        #print "*********** Coinjam: ",coin.s, coin.factores
        salida.write("%s %s\n" % (coin.s, " ".join(map(str,coin.factores))))
        J=J-1
        for base in xrange(2,11):
            coin.to_base(base)
            f = coin.get_factor()
            #print "en base",base,"es",coin.convertido,"divisible entre",f

    if coin.s == '1' * N:
        break

    coin.inc()


