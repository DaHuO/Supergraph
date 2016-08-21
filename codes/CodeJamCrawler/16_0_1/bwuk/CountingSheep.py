#Counting sheep
def CountSheep(n):
    orig = n
    digitsSeen = [0] * 10
    if n == 0:
        return -1
    loops = 0
    while loops < 1000:
        temp = n
        while temp > 0:
            digitsSeen[temp%10] = 1
            temp = temp//10
        
        if 0 not in digitsSeen:
            break
        n += orig

    return n
    
def main():
    f = open('A-large.in', 'r')
    numCases = int(f.readline())

    for i in range(1, numCases+1):
        n = int(f.readline())
        result = CountSheep(n)
        if result < 0:
            result = 'INSOMNIA'
        print('Case #', i, ': ', result, sep='')

main()
