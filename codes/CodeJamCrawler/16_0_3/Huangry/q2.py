import math

bases = range(2, 11)

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def fromStr(str, base):
    total = 0
    for i, value in enumerate(reversed(str)):
        total += int(value)*(base**i)
    return total

with open('test', 'r') as f:
    with open('q3solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            answer = ''
            line = f.readline().split()
            N, J = int(line[0]), int(line[1])
            for i in range(J):
                base_2 = toStr(i, 2)
                coin_part = '1' + '0'*int((N/2 - 2 - len(base_2))) + base_2 + '1'
                coin = coin_part*2
                answer += coin + ' '
                divisors = [fromStr(coin_part, base) for base in bases]
                for divisor in divisors:
                    answer += str(divisor) + ' '
                answer += '\n'
            solution.write('Case #' + str(case+1) + ': ' + '\n' + answer)

        solution.closed
    f.closed