from math import sqrt
def taskC():
    lines = [line.rstrip('\n') for line in open('C-small-attempt0.in')]
    target = open('answer2.out', 'w')
    N, J = (int(s) for s in lines[1].split())
    
    maxNum = int('1'*(N-2),2)
    count = 0
    lines = 0
    target.write("Case #1:\n")
    primes = []
    while count <= maxNum:
        if lines == J:
            break
        number = bin(count)[2:]
        if len(number) < N-2:
            number = '0'*(N-2-len(number))+number
        number = '1' + number +'1'
        rep = 2
        div = ""
        length = 0
        while rep <= 10:
            value = 0
            for i in range(len(number)):
                value += int(number[i])*(rep**(len(number)-1-i))
            for j in range(2, int(sqrt(value))):
                if value % j == 0:
                    div = div + str(j) + " "
                    length += 1
                    break
            rep += 1
        if length == 9:
            target.write(str(number) + " " + div[:-1] + "\n")
            lines += 1
        count += 1
