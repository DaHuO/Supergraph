"""
Revenge of the Pancakes

T is number of test cases

1 <= T <= 100

S is string of pancakes (+ or -) represents pancakes from top to bottom

1 <= length of S <= 10  Small Dataset
1 <= length of S <= 100 Large Dataset

y is minimum number of times to flip to get all pancakes happy side up
"""

input_file_name = 'B-large.in'
output_file_name = 'B_large_pancakes.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

def flip(pancake):
    if pancake == '+':
        return '-'
    else:
        return '+'    

def allHappy(pancakes):
    return '-' not in pancakes

def rangeOfSame(pancakes):    
    length = 0
    top = pancakes[0]
    for p in pancakes:
        if p == top:
            length += 1
        else:
            break
    return length      


for t in range(T):
    S = f.readline()    
    S = S.strip()   
    # print S 
    # convert S to a list of characters
    pancakes = list(S)
    count = len(pancakes)

    flipCount = 0
    
    if (allHappy(pancakes)):
        print 'Case #%d:' % (t+1), flipCount
        outFile.write('Case #' + str(t+1) + ': ' + str(flipCount) + "\n")
        # print 'all happy :) with %d flips' % flipCount    

    else:
        top = pancakes[0]
        if count == 1:
            pancakes[0] = flip(top)
            flipCount += 1
            if (allHappy(pancakes)):
                # print 'all happy :) with %d flips' % flipCount
                print 'Case #%d:' % (t+1), flipCount
                outFile.write('Case #' + str(t+1) + ': ' + str(flipCount) + "\n")
        else:        
            done = allHappy(pancakes)           
            while (not done):
                # print 'pancakes', pancakes
                top = pancakes[0]            
                allSame = True
                idx = 0
                
                r = rangeOfSame(pancakes)
                # print 'range = %d' % r
                
                # flip the ones that are the same all at once.
                for x in range(r):
                    pancakes[x] = flip(pancakes[x])

                flipCount += 1                      

                # print 'after flip:', pancakes
                done = allHappy(pancakes)
                # print 'done = ', done   

            # print 'flipCount = %d' % flipCount         
        
            print 'Case #%d:' % (t+1), flipCount
            outFile.write('Case #' + str(t+1) + ': ' + str(flipCount) + "\n")     