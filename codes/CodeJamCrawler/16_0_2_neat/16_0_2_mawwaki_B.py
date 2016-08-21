# -*-coding:utf-8 -*-

# def flip(S,i):
#     return "".join(["+" if S[i-j-1] =="-" else "-" for j in range(i)]) + S[i:]
#
#
# print(flip('--+-',4))

def inverse(side):
    return "+" if side =="-" else "-"

def rec_main_func(S,target):
    if not(S): # if S is empty
        return 0
    elif S[-1] == target:
        return rec_main_func(S[:-1],target)
    else:
        return 1 + rec_main_func(S[:-1],inverse(target))

def main_func(S):
    return str(rec_main_func(S,'+'))

# print(main_func('--+-'))

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
                case_listing[i]
            ]
            for i in case_indices
        ]
    output_string = "\n".join([ "Case #"+str(i+1)+": "+main_func(*inp) for i,inp in enumerate(formatted_input) ])
    print("output:")
    print(output_string)
    with open("output.txt","w") as output_file:
        output_file.write(output_string)