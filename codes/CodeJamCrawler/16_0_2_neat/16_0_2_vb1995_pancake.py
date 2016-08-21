#Varun Bharadwaj

pancakes = []

# change + to 1 and - to 0
def preprocess(ipstring):
    for i in ipstring.strip():
        if i=='+':
            pancakes.append(True)
        else:
            pancakes.append(False)

# flips n pancakes from the top of the stack
def flip(n):
    i = 0
    j = n-1
    while i<=j:
        if i==j:
            pancakes[i] = not pancakes[i]
            return
        pancakes[i],pancakes[j] = not pancakes[j],not pancakes[i]
        i = i + 1
        j = j - 1

# find minimum number of flips required 
def num_flips():
    num_of_flips = 0
    l = len(pancakes)-1
    while l>=0:
        if pancakes[l]:
            l = l-1
        else:
            if pancakes[0]:
                t = l-1
                while not pancakes[t]:
                    t = t-1
                flip(t+1)
                flip(l+1)
                num_of_flips = num_of_flips + 2
            else:
                flip(l+1)
                num_of_flips = num_of_flips + 1

            l = l-1
    return num_of_flips
            
    

testcases = int(input())

for tc in range(1,testcases+1):
    pancakes.clear()
    ipstring = input()
    preprocess(ipstring)
    print('Case #',tc,': ',num_flips(),sep='')
    
    

            
