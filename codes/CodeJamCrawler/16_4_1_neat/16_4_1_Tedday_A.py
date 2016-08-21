level = __file__.split("\\")[-1][0]
file_is_small = 1
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

letters = "PRS"
def reduce_lineup(lineup):
    reduce_map = {'RP':'P','PR':'P','SP':'S','PS':'S','SR':'R','RS':'R'}
    return "".join([reduce_map[lineup[i:i+2]] if lineup[i:i+2] in reduce_map else '0' for i in xrange(0,len(lineup),2) ])
    
    
def test_case():
    [N,R,P,S] = [int(i) for i in input_file.readline().split()]
    num = 2**N
    for i in xrange(3**num):
        s = ""
        for j in xrange(num):
            s = letters[i % 3] + s
            i /= 3
        t = s + ""
        if(s.count("R") == R and s.count("S") == S and s.count("P") == P):
            while(len(s) > 1 and not '0' in s):
                s = reduce_lineup(s)
            if(len(s) == 1 and s != "0"):
                return t
    return "IMPOSSIBLE"
        

T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
input_file.close()
output_file.close()
