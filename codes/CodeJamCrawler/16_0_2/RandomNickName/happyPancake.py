
def flip2(s):
    current = s[0]
    counter = 0
    if len(s) == 1:
        if current == '-':
            return 1
    for letter in s:
        if letter != current:
            current = letter
            counter = counter + 1
    return counter


def flip (s) :
    #print s.rfind('-')
    last = s.rfind('-')
    counter = 0
    while last != -1:
        counter = counter + 1
        right_side = s[last+1:]
        tmp = s[:last+1].replace('+', 'A')
        tmp = tmp.replace('-', '+')
        tmp = tmp.replace('A', '-')
        s = tmp + right_side
        last = s.rfind('-')
    #print s
    return counter

    

def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    #l, d, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print l,d,n

    for j in xrange(1, t+1):
        s = str(raw_input())  # read a list of integers, 2 in
        #k tiles, 
        #c complexity (number of levels = c + 1)
        #s grad students
        #print s
        answer = -1
        answer = flip(s)
        #answer = flip2(s)
        print "Case #{}: {}".format(j, answer) 
        
        
            
        

if __name__ == "__main__" :
    main()
