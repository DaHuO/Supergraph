import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

#input_file = 'input.txt'
#output_file = 'output.txt'

in_file = open(input_file)
out_file = open(output_file,'w')

line_counter = 0

def flip(L,index):
    for n,i in enumerate(L):
        if n >= index:
            if i == '+':
                L[n] = '-'
            else:
                L[n] = '+'

for line in in_file:
    maneuver = 0
    if line_counter > 0:
#         print line.rstrip()
        input_list = line.rstrip()
        input_list = list(input_list)
        input_list = input_list[::-1]
        while True:
            if '-' in input_list:
                maneuver+=1
                idx = input_list.index('-')
                flip(input_list,idx)
            else:
                break
#         print("Case #{}: {}".format(line_counter,maneuver))
        out_file.writelines("Case #{}: {}\n".format(line_counter,maneuver))
    line_counter+=1
out_file.close()