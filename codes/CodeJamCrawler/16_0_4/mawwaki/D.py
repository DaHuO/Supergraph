# -*-coding:utf-8 -*-
import math

# def main_func(K,C,S): # for S <= K # Produces incorrect result for some reason
#     if C*S < K: # <=> S < math.seil(K/C):
#         return "IMPOSSIBLE"
#     else:
#         theRightPosition = sum(( (i-1)*(K**(C-i)) for i in range(2,min(C,K)+1) ))
#         shift = C*(K**(C-1))
#         return " ".join( ( str(theRightPosition + alpha*shift + 1) for alpha in range(math.ceil(K/C)) ) )

def main_func(K,C,S): # for S == K
    return " ".join( ( str( (i-1)*(K**(C-1)) + 1 ) for i in range(1,S+1) ) )

# print(main_func(3,2,2))

hl = 1 # "Header lines" :Number of lines at the begining of the input file (haeder information)
lpc = 1 # "Lines per test case" number of lines foe each entry of input
ligne_sep = "\n" # Line separator
col_sep = " " # column seperatot

with open("input.txt",'r') as input_file:
    case_listing = input_file.read().split(ligne_sep)
    while case_listing[-1] == '' : del case_listing[-1] # Deleting all empty lines at the end
    C = int(case_listing[0]) # Number of test cases
    case_indices = [i+hl for i in range(C*lpc) if i%lpc == 0] # The indices of the first lines of every test case

    formatted_input = \
        [
            [
                int(num) for num in case_listing[i].split(col_sep)
            ]
            for i in case_indices
        ]
    output_string = "\n".join([ "Case #"+str(i+1)+": "+main_func(*inp) for i,inp in enumerate(formatted_input) ])
    print("output:")
    print(output_string)
    with open("output.txt","w") as output_file:
        output_file.write(output_string)