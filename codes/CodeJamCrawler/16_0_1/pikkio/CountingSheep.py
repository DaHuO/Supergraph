input_file = open("A-large.in", "r")
output_file = open("results.txt", "w+")

T = int(input_file.readline())

for i in range(0, T):
    number_str = input_file.readline().strip()
    number = int(number_str)
    if (number == 0):
        output_file.write("Case #" + str(i+1) + ": INSOMNIA\n")
        continue
    
    board = [ False for _ in range(10) ]
    digits = [ ]
    for j in range(len(number_str)):
        digits.append(int(number_str[len(number_str) - 1 - j]))
        board[digits[j]] = True
    
    summation = [ 0 for _ in range(len(digits) + 1) ]
    
    multiplier = 0
    board_complete = False
    while (not board_complete):
        multiplier += 1
        
        carry = 0
        for j in range(0, len(digits)):
            s = summation[j] + digits[j] + carry
            carry_next = 0
            if (s > 9):
                carry_next = 1
                s -= 10
            
            summation[j] = s
            board[summation[j]] = True
            carry = carry_next
        
        summation[len(digits)] += carry
        if (summation[len(digits)] > 0):
            board[summation[len(digits)]] = True
        
        board_complete = True
        for d in range(len(board)):
            if (not board[d]):
                board_complete = False        
    
    output_file.write("Case #" + str(i+1) + ": " + str(multiplier * number) + "\n")
    
input_file.close()
output_file.close()