
# coding: utf-8

# In[8]:

def problem_A(infileName, outputName):
    infile = open(infileName, 'r')
    outfile = open(outputName, 'w')
    
    lines = infile.readlines()
    
    for i in range(1, len(lines)):
        N = int(lines[i])
        output = "Case #" + str(i)
        if N == 0:
            output += ": INSOMNIA\n"
            outfile.write(output)
            continue
        digits = set()
        j = 0
        num = 0
        while len(digits) < 10:
            j += 1
            num = j * N            
            number = str(num)
            for d in number:
                digits.add(d)        
        output += ": " + str(num) + "\n"
        outfile.write(output)

problem_A("A-small-attempt0.in", "A_small_out")
        


# In[ ]:



