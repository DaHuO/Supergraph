import itertools
T = int(input())
nums = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
for t in range(T):
    S = list(input())
    phoneN = ""
    while 'Z' in S:
        phoneN += '0'
        for n in nums[0]:
            S.remove(n)
    while 'W' in S:
        phoneN += '2'
        for n in nums[2]:
            S.remove(n)
    while 'X' in S:
        phoneN += '6'
        for n in nums[6]:
            S.remove(n)
    while 'G' in S:
        phoneN += '8'
        for n in nums[8]:
            S.remove(n)
    while 'U' in S:
        phoneN += '4'
        for n in nums[4]:
            S.remove(n)
    while 'F' in S:
        phoneN += '5'
        for n in nums[5]:
            S.remove(n)
    while 'O' in S:
        phoneN += '1'
        for n in nums[1]:
            S.remove(n)
    while 'I' in S:
        phoneN += '9'
        for n in nums[9]:
            S.remove(n)
    while 'T' in S:
        phoneN += '3'
        for n in nums[3]:
            S.remove(n)
    while 'S' in S:
        phoneN += '7'
        for n in nums[7]:
            S.remove(n)
    phoneN = sorted(phoneN)
    print("Case #"+str(t+1)+": "+"".join(phoneN))
                
