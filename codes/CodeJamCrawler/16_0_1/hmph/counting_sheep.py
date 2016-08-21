def count_sheep(n):
    if (n == 0):
        return "INSOMNIA", 0
        
    seen = [0]*10
    i = 1
    
    while (i < 99999999999999999):
        
        number = i * n
        number_string = str(number)
        
        for char in number_string:
            digit = int(char)
            seen[digit] = 1
        
        if ( sum(seen) == 10 ):
            return number, i    
        i = i + 1           

def main():

    infile = 'input.txt'
    f = open(infile, 'r')
    lines = f.readlines()
    
    T = int(lines[0])
    #T = int(1e6)
    
    for i in range(T):
        n = int(lines[i+1])
        #n = i
        answer, index = count_sheep(n)
        
        print 'Case #'+str(i+1)+': '+str(answer)
        
main()