numCases = int(raw_input())
testCases = []

for i in range(numCases):
    testCases.append(int(raw_input()))
    
for num in range(numCases):
    N = testCases[num]
    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for mult in range(1, 81):
        for digit in str(mult * N):
            if array[int(digit)] != 1:
                array[int(digit)] = 1
        #print array
        if array == [1]*10:
            print("Case #" + str(num + 1) + ": " + str(mult * N))
            break
    else:
        print("Case #" + str(num + 1) + ": INSOMNIA")
    
