import fileinput












# Globals
DIGITS = [0,1,2,3,4,5,6,7,8,9]




def find_last_number(n):
    if n == 0:
        # Special case for INSOMNIA
        return "INSOMNIA"

    d = {}
    for i in DIGITS:
        d[i] = False
        
    multiple = n
    
    while d:
        res = multiple
        t = multiple
        while t > 0 and d:
            digit = t % 10
            t /= 10
            if digit in d:
                del d[digit]
    
        multiple += n

    return res




if __name__ == "__main__":
    
    f = open('workfile', 'w')
    i = 1
    
    for line in fileinput.input():
        if fileinput.isfirstline():
            continue
            
        n = int(line)
        res = find_last_number(n)
        f.write("Case #" + str(i) + ": " + str(res) + "\n")
        i += 1
        
    f.close()