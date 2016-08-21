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
    problema_a()

if __name__ == '__main__':
    main()