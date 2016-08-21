
numTests = int(input())
for i in range(numTests):
    string = input()
    output = string[0]
    for j in range(1, len(string)):
        if ord(string[j]) < ord(output[0]):
            output += string[j]
        else:
            output = string[j] + output
    print("Case #" + str(i + 1) + ": " + output)
