def readfile(filename):
    textfile = open(filename, 'r')
    text = ''
    while True:
        read = textfile.readline()
        if not read:
            break
        text += read
    return text

def writefile(filename, text):
    textfile = open(filename, 'w')
    textfile.write(text)
    textfile.close()

def tobase10(string, base):
    base10 = 0
    for i in range(len(string)):
        base10 += base ** i * int(string[-i-1])
    return base10

def smf(val):
    factor = 2
    while factor < val:
        if not val % factor:
            return factor
        if factor > 100:
            return "abort"
        factor += 1
    return False

variables = [line for line in readfile("C-large.in").split("\n")[1:] if line != ""][0].split(" ")

length = int(variables[0])
amount = int(variables[1])

output = "Case #1:"

jamcoin = 2**(length-1) + 1

while amount > 0:
    base = 2
    factors = []
    while base <= 10:
        smallestfactor = smf(tobase10(bin(jamcoin)[2:], base))
        if not smallestfactor:
            valid = False
            break
        factors.append(smallestfactor)
        base += 1
        if base > 10: valid = True
    if valid and "abort" not in factors:
        output += "\n" + bin(jamcoin)[2:] + " " + " ".join([str(factor) for factor in factors])
        amount -= 1
    jamcoin += 2

writefile("output.txt", output)
