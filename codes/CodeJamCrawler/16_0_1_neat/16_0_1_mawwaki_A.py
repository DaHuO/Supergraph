# -*-coding:utf-8 -*-


def main_func(N):
    if N == 0:
        return 'INSOMNIA'
    else:
        seenDigits = set()
        curr = 0
        while len(seenDigits) < 10: # normaly i shouldn't exceed 100
            curr += N
            for digit in str(curr):
                seenDigits.add(digit)
            # print(N, ":: ",curr," : ", sorted(list(seenDigits)) )

        return str(curr)


# print(main_func(11))


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
                int(case_listing[i])
            ]
            for i in case_indices
        ]
    output_string = "\n".join([ "Case #"+str(i+1)+": "+main_func(*inp) for i,inp in enumerate(formatted_input) ])
    print("output:")
    print(output_string)
    with open("output.txt","w") as output_file:
        output_file.write(output_string)