nums = {
    0:'ZERO', 
    2:'TWO', 
    4:'FOUR', 
    6:'SIX', 
    8:'EIGHT', 
    1:'ONE', 
    3:'THREE', 
    5:'FIVE', 
    7:'SEVEN', 
    9:'NINE', 
}

first_round = {
    'Z':0,
    'W':2,
    'U':4,
    'X':6,
    'G':8
}
second_round = {
    'O':1,
    'R':3,
    'F':5,
    'S':7
}
loner = 9

def solve(s):
    count = [0] * 26
    for character in s:
        count[ord(character) - ord('A')] += 1

    ans = [0] * 10


    for letter, value in first_round.iteritems():
        while count[ord(letter) - ord('A')]:
            ans[value] += 1
            for lets in nums[value]:
                count[ord(lets) - ord('A')] -= 1
    for letter, value in second_round.iteritems():
        while count[ord(letter) - ord('A')]:
            ans[value] += 1
            for lets in nums[value]:
                count[ord(lets) - ord('A')] -= 1
    while count[ord('N') - ord('A')]:
        ans[loner] += 1
        for lets in nums[loner]:
            count[ord(lets) - ord('A')] -= 1

    result = ""
    for i, num in enumerate(ans):
        result += "{}".format(i) * num
    return result


t = int(raw_input())

for test in xrange(t):
    print "Case #{}: {}".format(test+1, solve(raw_input()))