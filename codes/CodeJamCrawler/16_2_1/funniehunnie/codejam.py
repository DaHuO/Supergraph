for a in range(int(input().strip())):
    num = [0 for x in range(10)]
    letters = [0 for x in range(26)]
    for i in input().strip():
        letters[ord(i)-65] += 1
    for i in range(letters[25]): # Z
        num[0] += 1
        letters[25] -= 1
        letters[4] -= 1
        letters[17] -= 1
        letters[14] -= 1
    for i in range(letters[22]):
        num[2] += 1
        letters[19] -= 1
        letters[22] -= 1
        letters[14] -= 1
    for i in range(letters[20]):
        num[4] += 1
        letters[5] -= 1
        letters[14] -= 1
        letters[20] -= 1
        letters[17] -= 1
    for i in range(letters[5]):
        num[5] += 1
        letters[5] -= 1
        letters[8] -= 1
        letters[21] -= 1
        letters[4] -= 1
    for i in range(letters[14]):
        num[1] += 1
        letters[14] -= 1
        letters[13] -= 1
        letters[4] -= 1
    for i in range(letters[23]):
        num[6] += 1
        letters[18] -= 1
        letters[8] -= 1
        letters[23] -= 1
    for i in range(letters[6]):
        num[8] += 1
        letters[4] -= 1
        letters[8] -= 1
        letters[6] -= 1
        letters[7] -= 1
        letters[19] -= 1
    for i in range(letters[7]):
        num[3] += 1
        letters[19] -= 1
        letters[7] -= 1
        letters[17] -= 1
        letters[4] -= 2
    for i in range(letters[21]):
        num[7] += 1
        letters[18] -= 1
        letters[4] -= 2
        letters[21] -= 1
        letters[13] -= 1
    for i in range(letters[8]):
        num[9] += 1
        letters[13] -= 2
        letters[8] -= 1
        letters[4] -= 1
        
    answer = ''
    for i in range(10):
        for j in range(num[i]):
            answer += str(i)
    print('Case #' + str(a+1) + ': ' + answer)
