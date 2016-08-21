import sys




def simplify_cakes(cakes):
    current_cake = cakes[0]
    new_cakes = current_cake
    for idx in range(1,len(cakes)):
        if current_cake != cakes[idx]:
            current_cake = cakes[idx]
            new_cakes += current_cake

    return new_cakes

def calculate_operations(new_cakes,operation):
    #print new_cakes,operation
    if(new_cakes == "-"):
        
        return operation+1
    elif(new_cakes == "+"):
        return operation
    elif(new_cakes[0] == "-"):
        return calculate_operations(new_cakes[1:],operation+1)
    elif(new_cakes[0] == "+"):
        return calculate_operations(new_cakes[1:],operation+1)
    

if __name__ == "__main__":
    #nputf = sys.argv[1]
    inputfname = "B-large.in"
    inputf = open(inputfname)
    caseNumb = inputf.readline()
    #print caseNumb

    outputfile = open('output','a')

    for i in range(1,int(caseNumb)+1):
        cakes = inputf.readline()
        cakes = cakes.rstrip('\n')
        #print cakes,len(cakes)
        new_cakes = simplify_cakes(cakes)
        #print new_cakes
        ans = calculate_operations(new_cakes,0)
        print ans
        ans_str = "Case #" + str(i) + ": " + str(ans) + "\n"
        outputfile.write(ans_str)

    outputfile.close()
