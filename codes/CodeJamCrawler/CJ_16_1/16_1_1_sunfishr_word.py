"""
The Last Word

T test cases

Each test case has one line with string S

Small dataset:
1 <= S <= 15

Large dataset:
1 <= S <= 1000

"""

input_file_name = 'A-large.in'
output_file_name = 'A-large_word.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

for t in range(T):
    S = f.readline().strip()    
    count = len(S)    
    # print S
    letters = list(S)

    high = letters[0]    
    output = ''
    for ch in letters:
        if (ch >= high):
            high = ch
            output = high + output
        else:
            output += ch

    print 'Case #%d:' % (t+1), output
    outFile.write('Case #' + str(t+1) + ": " + output + "\n")     
    


        

    

    
