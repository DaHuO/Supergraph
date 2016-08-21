__author__ = 'KH2006'

t = int(input())  # read a line with a single integer1
for testCase in range(1, t + 1):

    numbers = ['ZERO', 'TWO', 'FOUR','SIX', 'EIGHT', 'ONE','THREE',
               'FIVE', 'SEVEN', 'NINE']

    nums = [0, 2,4,6,8,1,3,5,7,9]

    inputForTestcase = input()

    inputs = [letter for letter in inputForTestcase]

    output = ""
    count = 0
    current = 0

    for num in numbers:
        literal = num[0]

        if inputs.count(literal) > 0:
            while True:
                numFound = True
                found = True
                temp = inputs[:]
                for letter in num:
                    if temp.count(letter) > 0:
                        index = temp.index(letter)
                        temp[index] = '?'
                    else:
                        numFound = False
                        found = False
                        break

                if found:
                    count += len(num)
                    inputs = temp
                    output += str(nums[current])

                if not numFound:
                    break

        if count == len(inputs):
            break

        current += 1

    print("Case #{}: {}".format(testCase, ''.join(sorted(output))))