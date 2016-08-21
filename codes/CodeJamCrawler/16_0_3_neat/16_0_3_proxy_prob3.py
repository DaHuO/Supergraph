outfile = open("output3", "w")

N = 32
J = 500

outfile.write("Case #1:\n")

def is_prime(n):
    if n == 2 or n == 3:
        return -1
    if n < 2 or n % 2 == 0:
        return 2
    if n < 9:
        return -1
    if n % 3 == 0:
        return 3
    r = 10000
    dia = 5
    while dia <= r:
        if n % dia == 0:
            return dia
        if n % (dia + 2) == 0:
            return dia + 2
        dia += 6
    return -1

x = 0
count = 0

while count < J:
    binary = "%030d" % (int(bin(x)[2:]),)
    binary = '1{0}1'.format(binary)
    divs = []
    for base in range(2,11):
        num = 0
        temp_base = 1
        for bit in reversed(binary):
            num += int(bit)*(temp_base)
            temp_base *= base
       
        div = is_prime(num)
        if div != -1:
            divs.append(div)
        else: break

    if len(divs) == 9:
        count += 1
        outfile.write(binary),
        for div in divs:
            outfile.write(" "+str(div)),
        outfile.write("\n")
    x += 1
