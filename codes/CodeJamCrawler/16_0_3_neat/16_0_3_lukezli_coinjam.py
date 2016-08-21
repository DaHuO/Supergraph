N = 16
J = 50


def interp(bin_vals, base):
    accum = 0
    for i in bin_vals:
        accum = accum * base
        accum += i
    return accum

def valid_factor(val):
    i = 2
    while i * i <= val:
        if val % i == 0:
            return i
        i += 1
    return None

def factors(bin_str):
    bin_vals = [int(a) for a in list(bin_str)]
    factor_vals = []
    for base in range(2,11):
        base_val = interp(bin_vals,base)
        factor = valid_factor(base_val)
        if factor == None:
            return None
        else:
            factor_vals.append(factor)
    return factor_vals

print "Case #1:"

for i in range (2**(N-2)):
    if J == 0: break
    
    num = (1 << 15) + (i << 1) + 1
    bin_str = "{0:b}".format(num)

    factor_vals = factors(bin_str)
    if factor_vals != None:
        print bin_str, " ".join(str(val) for val in factor_vals)
        J -= 1

        
