import sys, itertools

input_file_name = 'A-large.in'
output_file_name = 'output1large.txt'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

contents = f_in.readlines()
num_cases = int(contents.pop(0))

def digitize(n):
    number_string = str(n)
    digits = []
    for ch in number_string:
        digits.append(ch)
    return digits

def count(n):
    tracker = [0,0,0,0,0,0,0,0,0,0]
    i = 1
    j = n
    if j == 0:
        return "INSOMNIA"
    else:
        while True:
            digits = digitize(j)
            for d in digits:
                tracker[int(d)] = 1
            if 0 not in tracker:
                break
            else:
                i = i + 1
                j = n * i
    number = ''.join(digits)
    return(number)

for case in range (num_cases):

    N = contents.pop(0)
    NUM = int(N)
    answer = count(NUM)

    print('Case #{}: {}'.format(case+1, answer))
    print('Case #{}: {}'.format(case+1, answer), file = f_out)
  
f_in.close()
f_out.close()
