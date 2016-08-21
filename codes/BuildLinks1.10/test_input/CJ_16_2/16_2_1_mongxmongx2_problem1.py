import fileinput

def pan_cake(Cake):
    return count

if __name__ == "__main__":

    input_file = open("A-large.in")
    output_file = open("A-large.out","w")

    T  = int(input_file.readline())
    #T  = input()
    result = [[]]
    
    for i in range(T):
        S = input_file.readline()
        #S = raw_input()
        
        # [Z, W, U, F, X, G, S, O, N, E, R,   T,   H,   V,   I]
        # [0, 1,   2, 3, 4, 5, 6,  7,  8, 9,10,11,12,13,14] 
        count = [0] * 16
        result_array=[]
            
        for j in range(len(S)):
            if S[j] == "Z":
                count[0] += 1
            if S[j] == "W":
                count[1] += 1
            if S[j] == "U":
                count[2] += 1
            if S[j] == "F":
                count[3] += 1
            if S[j] == "X":
                count[4] += 1
            if S[j] == "G":
                count[5] += 1
            if S[j] == "S":
                count[6] += 1
            if S[j] == "O":
                count[7] += 1
            if S[j] == "N":
                count[8] += 1
            if S[j] == "E":
                count[9] += 1
            if S[j] == "R":
                count[10] += 1
            if S[j] == "T":
                count[11] += 1
            if S[j] == "H":
                count[12] += 1
            if S[j] == "V":
                count[13] += 1
            if S[j] == "I":
                count[14] += 1

        # Test Case
        # ZERO
        while(count[0]!=0):
            result_array.append(0)
            count[0] -= 1
            count[7] -= 1
            count[9] -= 1
            count[10] -= 1
        # TWO
        while(count[1]!=0):        
            result_array.append(2)
            count[1] -= 1
            count[7] -= 1
            count[11] -= 1
        # FOUR
        while(count[2]!=0):        
            result_array.append(4)
            count[2] -= 1
            count[3] -= 1
            count[7] -= 1
            count[11] -= 1
        # SIX
        while(count[4]!=0):        
            result_array.append(6)
            count[4] -= 1
            count[6] -= 1
            count[14] -= 1
         # EIGHT
        while(count[5]!=0):        
            result_array.append(8)
            count[5] -= 1
            count[9] -= 1
            count[11] -= 1
            count[12] -= 1
            count[14] -= 1
         # ONE
        while(count[7]!=0):        
            result_array.append(1)
            count[7] -= 1
            count[8] -= 1
            count[9] -= 1
         # THREE
        while(count[12]!=0):        
            result_array.append(3)
            count[9] -= 2
            count[10] -= 1
            count[11] -= 1
            count[12] -= 1
         # FIVE
        while(count[3]!=0):        
            result_array.append(5)
            count[3] -= 1
            count[9] -= 1
            count[13] -= 1
            count[14] -= 1
         # SEVEN
        while(count[6]!=0):        
            result_array.append(7)
            count[6] -= 1
            count[8] -= 1
            count[9] -= 2
            count[13] -= 1
         # NINE
        for j in range(count[14]):
            result_array.append(9)
        
        # Sort
        result_array.sort()

        # print
        rr = ""
        for j in range(len(result_array)):
            rr += str(result_array[j])
        #print ("Case #"+str(i+1)+": "+rr)
        output_file.write("Case #"+str(i+1)+": " + rr + "\n")
    output_file.close()
    
