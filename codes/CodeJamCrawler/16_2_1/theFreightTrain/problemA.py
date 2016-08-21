def solve(S):
    letterCounts = {}
    for letter in list(S):
        if letter in letterCounts:
            letterCounts[letter] = letterCounts[letter] + 1
        else:
            letterCounts[letter] = 1
    #print(letterCounts)
    digits = [0]*10
    if 'Z' in letterCounts:
        digits[0] = letterCounts['Z']
        letterCounts['R'] -= digits[0]
        letterCounts['O'] -= digits[0]
    if 'W' in letterCounts:
        digits[2] = letterCounts['W']
        letterCounts['O'] -= digits[2]
    if 'U' in letterCounts:
        digits[4] = letterCounts['U']
        letterCounts['F'] -= digits[4]
        letterCounts['R'] -= digits[4]
        letterCounts['O'] -= digits[4]
    if 'X' in letterCounts:
        digits[6] = letterCounts['X']
        letterCounts['S'] -= digits[6]
        letterCounts['I'] -= digits[6]
    if 'G' in letterCounts:
        digits[8] = letterCounts['G']
        letterCounts['I'] -= digits[8]
    if 'R' in letterCounts:
        digits[3] = letterCounts['R']
    if 'F' in letterCounts and letterCounts['F']>0:
        digits[5] = letterCounts['F']
        letterCounts['I'] -= digits[5]
    if 'S' in letterCounts:
        digits[7] = letterCounts['S']
    if 'O' in letterCounts:
        digits[1] = letterCounts['O']
    if 'I' in letterCounts:
        digits[9] = letterCounts['I']
    #print(digits)
    returnString = '0'*digits[0]+'1'*digits[1]+'2'*digits[2]+'3'*digits[3]+'4'*digits[4]+\
    '5'*digits[5] + '6'*digits[6] + '7'*digits[7] + '8'*digits[8] + '9'*digits[9]
    return returnString

for i in range(1,int(input())+1):
    S = input()
    print('Case #{}: {}'.format(i,solve(S)))