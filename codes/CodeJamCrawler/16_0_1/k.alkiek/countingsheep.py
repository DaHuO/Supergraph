T = int(raw_input())  # read number of cases
nums = [0,1,2,3,4,5,6,7,8,9]

def elementsofin(L,ref): #function to compare seen with all numbers
    x = [i for i in ref if i in L]
    if x == ref:
        return True
    else:
        return False

for i in xrange(1, T + 1):
    N = int(raw_input()) # read chosen N
    
    if N == 0:
        output = "INSOMNIA"
    else:
        seen = []
        z=0
        while not(elementsofin(seen,nums)):
            z+=1
            listofN = map(int, str(N*z)) # convert product into an array

            for j in listofN: #add digits of product as seen numbers
                seen.append(j)
        output = N*z


    print "Case #{}: {}".format(i, output)


