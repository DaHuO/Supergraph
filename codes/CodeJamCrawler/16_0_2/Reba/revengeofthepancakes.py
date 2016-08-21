###
 # Google Code Jam
 # Author Rebecca Chen
###
 
input_file = open('B-large.in', 'r')
output_file = open('B-large.out', 'w')
 
num_cases = int(input_file.readline())

pmap = {'+': '-', '-': '+'}
 
for i in range(num_cases):
    output_file.write('Case #' + str(i+1) + ': ')
     
    pancakes = input_file.readline().replace('\n', '')
    num_moves = 0
    while len(pancakes) > 0:
        if pancakes[-1] == '+':
            pancakes = pancakes[:-1]
        elif pancakes[0] == '-' and pancakes[-1] == '-':
            num_moves += 1
            pancakes = [pmap[p] for p in reversed(pancakes)]
        else:
            num_moves += 1
            pancakes = [pmap[p] for p in pancakes]
    output_file.write(str(num_moves))

    output_file.write('\n')
     
input_file.close()
output_file.close()
