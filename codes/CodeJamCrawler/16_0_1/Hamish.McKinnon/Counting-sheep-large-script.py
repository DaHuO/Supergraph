import re
Input_file = open('Counting-sheep-large.txt', 'r')
Output_file = open('Counting-sheep-large-solution.txt', 'w')

Input = Input_file.read()
Input_file.close()
Input = Input.split('\n')

T = int(Input[0])
Output = [None] * T

for a in range(0, T):

    N = int(Input[a + 1])
    Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Digits_sum = 10
    A = 1
    
    if N == 0:
        Digits_sum = 0
        B = 'INSOMNIA'
    
    while Digits_sum > 0:
        B = str(A * N)
        for b in Digits:
            if b != 'Found':
                if re.search(str(b), B):
                    Digits_sum = Digits_sum - 1
                    Digits[int(b)] = 'Found'
        A = A + 1
        
    Output[a] = 'Case #' + str(a + 1) + ':' + ' ' + B

for z in range(0, len(Output)):
    Output_file.write(str(Output[z]) + '\n')

Output_file.close()