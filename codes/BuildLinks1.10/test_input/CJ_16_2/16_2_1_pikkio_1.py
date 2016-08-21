#index of char
def ic(c):
    return ord(c)-65

input_file = open("A-large.in", "r")
output_file = open("results.txt", "w+")

T = int(input_file.readline())

for i in range(0, T):
    s = input_file.readline().strip()
    
    chars = [ 0 ] * 26
    
    for c in s:
        chars[ic(c)] += 1
    
    numbers = [ 0 ] * 10
    
    # count zeros
    numbers[0] = chars[ic('Z')]
    chars[ic('Z')] -= numbers[0]
    chars[ic('E')] -= numbers[0]
    chars[ic('R')] -= numbers[0]
    chars[ic('O')] -= numbers[0]
    
    # count twos
    numbers[2] = chars[ic('W')]
    chars[ic('T')] -= numbers[2]
    chars[ic('W')] -= numbers[2]
    chars[ic('O')] -= numbers[2]
    
    # count fours
    numbers[4] = chars[ic('U')]
    chars[ic('F')] -= numbers[4]
    chars[ic('O')] -= numbers[4]
    chars[ic('U')] -= numbers[4]
    chars[ic('R')] -= numbers[4]
    
    # count sixes
    numbers[6] = chars[ic('X')]
    chars[ic('S')] -= numbers[6]
    chars[ic('I')] -= numbers[6]
    chars[ic('X')] -= numbers[6]
    
    # count eights
    numbers[8] = chars[ic('G')]
    chars[ic('E')] -= numbers[8]
    chars[ic('I')] -= numbers[8]
    chars[ic('G')] -= numbers[8]
    chars[ic('H')] -= numbers[8]
    chars[ic('T')] -= numbers[8]

    # count threes
    numbers[3] = chars[ic('H')]
    chars[ic('T')] -= numbers[3]
    chars[ic('H')] -= numbers[3]
    chars[ic('R')] -= numbers[3]
    chars[ic('E')] -= numbers[3]
    chars[ic('E')] -= numbers[3]

    # count sevens
    numbers[7] = chars[ic('S')]
    chars[ic('S')] -= numbers[7]
    chars[ic('E')] -= numbers[7]
    chars[ic('V')] -= numbers[7]
    chars[ic('E')] -= numbers[7]
    chars[ic('N')] -= numbers[7]

    # count ones
    numbers[1] = chars[ic('O')]
    chars[ic('O')] -= numbers[1]
    chars[ic('N')] -= numbers[1]
    chars[ic('E')] -= numbers[1]

    # count fives
    numbers[5] = chars[ic('V')]
    chars[ic('F')] -= numbers[5]
    chars[ic('I')] -= numbers[5]
    chars[ic('V')] -= numbers[5]
    chars[ic('E')] -= numbers[5]

    # count nines
    numbers[9] = chars[ic('I')]
    chars[ic('N')] -= numbers[9]
    chars[ic('I')] -= numbers[9]
    chars[ic('N')] -= numbers[9]
    chars[ic('E')] -= numbers[9]

    # now chars should be all zeros...
    
    result = "Case #" + str(i+1) + ": "
    for j in range(10):
        result += str(j) * numbers[j]

    output_file.write(result + "\n")

input_file.close()
output_file.close()
