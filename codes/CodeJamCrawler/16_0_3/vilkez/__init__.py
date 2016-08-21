# PRoblema C
from random import randint
import math
import datetime

# Todos los jamcoins
jamcoins = []
not_valid_jamcoins = []

#####################################################################
#####################################################################
class Jamcoin:
    def __init__(self, length):
        self.jamcoin = self.generate_random_jamcoin(length)
        #print("Intentando con jamcoin: ", self.jamcoin)
        
        while not self.is_jamcoin_valid():
            self.jamcoin = self.generate_random_jamcoin(length)
            #print("Intentando con jamcoin: ", self.jamcoin)
        
    def is_jamcoin_valid(self):
        # Antes que nada chequeo que no este entre los no validos ni los ya agregados
        if self.jamcoin in jamcoins or self.jamcoin in not_valid_jamcoins:
            return False
        
        self.non_trivial_divisors = []
        
        for i in range(2, 11):
            n = get_number_in_base(self.jamcoin, i)
            
            # Check de primo
            if is_prime(n):
                #print("Jamcoin no valido [PRIMO] ", self.jamcoin)
                not_valid_jamcoins.append(self.jamcoin)
                return False
            
            # Check de divisores
            divs = list(get_divisors(n))
            
            if len(divs) <= 2:
                #print("Jamcoin no valido [divisores] ", self.jamcoin)
                not_valid_jamcoins.append(self.jamcoin)
                return False
            
            # Como se que hay 3 o mas elementos, agarro el 2do elemento
            # Ya que garantiza que no sea trivial
            # Ej: n = 9 ... [1, 3, 9]
            # Ej: n = 6 ... [1, 2, 3, 6]
            self.non_trivial_divisors.append(divs[1])
            
        jamcoins.append(self.jamcoin)
        return True
    
    def generate_random_jamcoin(self, length):
        jamcoin = "1"
        
        for i in range(0, length-2):
            jamcoin += str(randint(0,1))
            
        return jamcoin + "1"

#####################################################################
#####################################################################

def get_divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def get_number_in_base(n, base):
    r = 0
    
    for i in range(0, len(n)):
        now = int(n[len(n) - i - 1])
        r += now * pow(base, i)
        
    return int(r)

def arr_to_str(arr):
    s = "";
    
    for i, a in enumerate(arr):
        s += str(a)
        if i < len(arr) - 1:
            s += " "
            
    return s

def problema_c():
    f = cargar_archivo("input")
    casos = f.readline()
    
    print("Comienza:", datetime.datetime.now().time())
    
    result = "Case #1: \n"
    
    for case_now, line in enumerate(f):
        n = int(line.split(' ')[0])
        j = int(line.split(' ')[1])
        
        for i in range(0, j):
            jamcoins.append(Jamcoin(n))
            #print("Jamcoin #" + str(i + 1) + ":", jamcoins[-1].jamcoin, "Con divisores:", jamcoins[-1].non_trivial_divisors)
            print("Jamcoin #" + str(i + 1) + ":", jamcoins[-1].jamcoin, "Con divisores:", arr_to_str(jamcoins[-1].non_trivial_divisors))
            result += jamcoins[-1].jamcoin + " "
            result +=  arr_to_str(jamcoins[-1].non_trivial_divisors) + "\n"


    print(result)
    guardar_archivo("output", result)
    print("Termina:", datetime.datetime.now().time())















# Problema B
def flip(a):
    a_ = ""
    flip = True
    
    flip_sign = "+" if a[0] == "+" else "-"
    
    for c in a:
        if c != flip_sign:
            flip = False             
        
        if flip:
            a_ += "+" if c == "-" else "-"
        else:
            a_ += c
            
    return a_
            
    
def problema_b():
    f = cargar_archivo("input")
    casos = f.readline()
    
    result = ""
    
    for case_now, line in enumerate(f):
        moves = 0
        case = line
        
        while True:
            # Chequeo si termino
            if "-" not in case:
               result += "Case #" + str(case_now + 1) + ": " + str(moves) + "\n"
               break 
            
            # Sino...
            if "-" in case:
                case = flip(case)
                moves += 1
                
    print(result)
    guardar_archivo("output", result)




















# Problema A
from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def add_n_to_str(n, s):
    m = str(n)
    
    for c in m:
        if c not in s:
            s += c
            
    return s

def problema_a():
    f = cargar_archivo("input")
    casos = f.readline()
    
    result = ""
    
    # Para controlar que no se quede en un loop infinito
    max_iterations_without_changes = 1000
    
    for case_now, line in enumerate(f):
        # El ultimo i donde hubo cambio
        i_last = 0
        
        n = int(line)
        
        if n == 0:
            result += "Case #" + str(case_now + 1) + ": INSOMNIA" + "\n"
            continue
        
        # El string que se usara para chequear si se durmio o no.
        all_numbers = add_n_to_str(n, "")
        
        # El multiplicador
        mult = 1
        
        while(True):
            all_numbers_before = all_numbers
            all_numbers = add_n_to_str(mult * n, all_numbers)
            
            # Control que no haya loop infinito
            if len(all_numbers_before) != len(all_numbers):
                i_last = case_now
                       
            if case_now - i_last > max_iterations_without_changes:
                result += "Case #" + str(case_now + 1) + ": INSOMNIA" + "\n"
                break
            
            # Reviso si termino
            if len(all_numbers) == 10:
                result += "Case #" + str(case_now + 1) + ": " + str(mult * n) + "\n"
                break
            
            mult += 1
                
    print(result)
    guardar_archivo("output", result)

# Funciones comunes
def cargar_archivo(filepath):
    f = open(filepath, 'r');
    return f;

def guardar_archivo(filepath, text):
    f = open(filepath, 'w')
    f.write(text)

def main():
    problema_c()

if __name__ == '__main__':
    main()