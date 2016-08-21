import sys

def last_num(num, j):
    if num == 0:
        print "Case #%d: INSOMNIA" % (j)
        return
        
    results = [0] * 10
    counter = 0
    i = 1
    N = abs(num)
    
    while True:                    
        N = num * i
        n = N
        
        while n > 0:
            digit = n % 10
            n = n / 10
            if results[digit] == 0:
                counter += 1
            results[digit] += 1
            
        if counter == 10:
            print "Case #%d: %d" % (j, N)
            return       
        i += 1
              

def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: python program.py < input')
    
    i = 1
    maximum = int(sys.stdin.readline())
    
    for l in sys.stdin:
        if i > maximum:
            break
            
        num = int(l)
        last_num(num, i)
        i += 1
    return

if __name__ == '__main__':
    main()
