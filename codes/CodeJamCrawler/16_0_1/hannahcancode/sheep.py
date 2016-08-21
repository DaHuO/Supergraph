I = open('A-large.in', 'r')
O = open('output.txt', 'w')
string = ""
L = []
cases = 0

N = I.readline()

for line in I:
    cases += 1
    digits = set()
    count = 1
    line = line.rstrip('\n')
    N = int(line)
    while digits != {'0','1','2','3','4','5','6','7','8','9'} and count < 500:
        number = N * count
        for char in str(number):
            digits.add(char)
        if count == 499:
            number = "INSOMNIA"
        count += 1
    O.write("Case #"+str(cases)+": "+str(number)+"\n")
I.close()
O.close()
    
