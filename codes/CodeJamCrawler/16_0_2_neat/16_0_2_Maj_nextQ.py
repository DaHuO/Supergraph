global input

def flipcake():
    y=0
    for i in input:
        if(input[y] == "+"):
            input[y] = "-"
        elif(input[y] == "-"):
            input[y] = "+"
        y+=1

nums = int(raw_input()) 
for i in xrange(1, nums + 1):
    input = str(raw_input())
  
    length = len(input)
    input = list(input[::-1])
    num = i
    j = 0
    flip_count = 0
  
    while j < length:
        if(input[j] == "-"):
            flipcake()
            flip_count +=1
  
        j+=1

    print "Case #{}:    {}".format(num, flip_count)
