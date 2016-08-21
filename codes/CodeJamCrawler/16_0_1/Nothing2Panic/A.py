import numpy as np
import sys

def counting_sheep(N):
    init_set = set()
    desti_set = set(['0','1','2','3','4','5','6','7','8','9' ])
    #print desti_set
    #desti_set.remove('1')
    #print desti_set

    if N == 0 :
        return 'INSOMNIA'
    
    i = 0;
    while len(desti_set) != 0 :
        i=i+1
        numbstr = str(i*N)
        #print numbstr
        for char in numbstr:
            if char in desti_set:
                #print char
                desti_set.remove(char)
                #print desti_set
    
    return str(i*N)


if __name__ == "__main__":
    file_name = sys.argv[1]
    print file_name
    A_input = np.genfromtxt(file_name,dtype='i4')
    #print A_input

    case_num = A_input[0]

    for idx in range(1,case_num+1):
        ans =  "Case #"+str(idx) + ": " + counting_sheep(A_input[idx])
        print ans
        with open('output','a') as outputFile:
            outputFile.write(ans + '\n')

    

