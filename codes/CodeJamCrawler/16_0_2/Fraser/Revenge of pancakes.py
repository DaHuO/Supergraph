def flip(s):
    flipped = ''
    for i in range(len(s)):
        if s[i] == '-':
            flipped +='+'
        else:
            flipped +='-'
    return flipped

def fast_flip(s):
    count = 0
    i = len(s) - 1
    while '-' in s and i>=0:
        if s[i] == '-':
            front = flip(s[:i + 1])
            s = front + s[i + 1:]
            count += 1
        i-=1
    return count
            
        
file = open('data6.txt','r')
my_results = open('results.txt','w')
t = int(file.readline())  # read a line with a single integer
for i in range(1, t + 1):
    s = str(file.readline().strip('\n')) # read a pancake
    print("Case #{}: {}\n".format(i, fast_flip(s)))
    my_results.write("Case #{}: {}\n".format(i, fast_flip(s)))
    # check out .format's specification for more formatting options
my_results.close()
file.close()