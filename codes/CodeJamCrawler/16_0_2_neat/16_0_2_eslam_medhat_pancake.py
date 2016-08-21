def main():
    #read in file
    File_tiny="tiny.in"
    File_small = "B-small-attempt0.in"
    File_large = "B-large.in"
    in_f = open(File_large, "r")
    t_cases = int( str.lstrip(in_f.next()) )

    #init out file
    out_f= open( "pancake_out.txt", "w" )

    


    #main loop
    for case in range(t_cases):

        stack = str.rstrip(in_f.next())
        #print "=================="
        #print stack
        #print "------------------"
        currentp=" "
        nextp=" "
        flips = 0
        for char in range(len(stack)):
            if (char == len(stack)-1) & (stack[char] == "+" ):
                out_f.write("Case #"+str(case+1)+": " + str(flips) +"\n")
            elif(char == len(stack)-1) & (stack[char] == "-" ):
                    stack = flip(stack, char)
                    flips = flips + 1
                    out_f.write("Case #"+str(case+1)+": " + str(flips) +"\n")
            else:
                currentp = stack[char]
                nextp = stack[char+1]
                if currentp != nextp:
                    stack = flip(stack, char)
                    flips = flips + 1
                    #print stack
        #print "==================="
    #close files
    in_f.close()
    out_f.close()
    return


def flip(stack, pos):
    temp = list(stack)
    for i in range(pos):
        if temp[i] == "+":
            temp[i] = "-"
        else:
            temp[i] = "+"
    return ''.join(temp)
