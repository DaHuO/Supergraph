
import sys

def get_factor(input_num):
    if not input_num & 1:
        return 2
    
    for x in range(3, int(input_num**0.5) + 1, 2):
        if input_num % x == 0:
            return x
    return None

def check_base(number_str):
    bases = range(2,11)
    
    factors = []
    for base in bases:
        new_num = int(number_str, base)
        new_factor = get_factor(new_num)
        if (not new_factor):
            return None
        factors.append(new_factor)
    return factors
    
def jam_coin(n,j):
    start_value = int("0" * (n -2),2)
    end_value = int("1" * (n - 2), 2)
    
    valid_number = 0
    
    for number in range(start_value, end_value + 1):
        new_num = format(number, "b")
        binary_number = "1" + "0"* (n -2 -len(new_num))+ new_num   + "1"
        
        factors = check_base(binary_number)
        if factors:
            valid_number = valid_number  + 1
            print "%s %s" % (binary_number, ' '.join(str(value) for value in factors))
            if (valid_number >= j):
                return 
    
if __name__ == '__main__':
    num_cases = int(sys.argv[1])
    
    for i in range(num_cases):
        print "Case #%s:" %(i + 1)
        n = int(sys.argv[i * 2 + 2])
        j = int(sys.argv[i * 2 + 3 ])        
        jam_coin(n,j)