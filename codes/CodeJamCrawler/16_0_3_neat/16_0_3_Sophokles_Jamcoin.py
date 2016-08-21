import itertools
def checker(candidate):
    for divisor in range(2,int((candidate+1) ** 0.5)):
        if candidate % divisor == 0:
            return divisor
    return 0

test = int(input())
rawInput = input().split()
coins = []
N = int(rawInput[0])
J = int(rawInput[1])
startText = '1' + (N-2) * '0' + '1'
startNum = int(startText)
count = 1
middles = []
for i in itertools.product([0,1],repeat=N-2):
    middles.append(''.join(map(str,i)))
while J > 0:
    print(startText)
    result = [startText]
    for base in range(2,11):
        converted = 0
        for column in range(N):
            converted += int(startText[column]) * (base ** (N-column-1))
        check = checker(converted)
        if check != 0:
            result.append(check)
    if len(result) == 10:
        coins.append(result)
        J -= 1
    startText = '1' + middles[count] + '1'
    count += 1
print("Case #{}:".format(test))
for i in coins:
    print(' '.join(map(str,i)))