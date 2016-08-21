def compress_string (string):
    
    if (len(string) == 0):
        raise AssertionError('String should not be empty')
    
    compressed = string[0]
    
    for char in string:
        if (char != compressed[-1] ):
            compressed = compressed + char
    
    return compressed
        
def solve (input):
    
    compress = compress_string(input)
       
    if (compress[-1] == '+'):
        compress = compress[0:-1]
        
    return len(compress)        
    
def main():
    
    inputfile = 'input.txt'
    f = open(inputfile, 'r')
    lines = f.readlines()
    
    T = int(lines[0])
    
    for i in range(T):
        input = lines[i+1].strip()
        
        answer = solve(input)
        print 'Case #'+str(i+1)+': '+str(answer)     
                                                                  
main()