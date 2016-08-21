marks = [
    ('Z', ('0', 'ZERO')),
    ('G', ('8', 'EIGHT')),
    ('X', ('6', 'SIX')),
    ('W', ('2', 'TWO')),
    ('S', ('7', 'SEVEN')),
    ('V', ('5', 'FIVE')),
    ('I', ('9', 'NINE')),
    ('F', ('4', 'FOUR')),
    ('H', ('3', 'THREE')),
    ('O', ('1', 'ONE')),
]
T = int(raw_input().split()[0])

class bucket:
    def __init__(self, s):
        if isinstance(s, dict):
            self.d = s
        else:
            self.d = {}
            for c in s:
                if c in self.d:
                    self.d[c] += 1
                else:
                    self.d[c] = 1

    def __mul__(self, num):
        new_d = {}
        for c in self.d:
            new_d[c] = self.d[c] * num
        return bucket(new_d)

    def __add__(self, b):
        new_d = {}
        for c in self.d:
            new_d[c] = self.d[c]
        for c in b.d:
            new_d[c] += b.d[c]
        return bucket(new_d)

for tt in range(T):
    S = raw_input()
    b = bucket(S)
    phone_number = []
    for mark in marks:
        if mark[0] in b.d:
            # print mark[0]
            num = b.d[mark[0]]
            # print(num)
            if num:
                b = b + bucket(mark[1][1]) * (-1*num)
                # print('aan')
                phone_number.extend([mark[1][0] * num])
                # print(phone_number)
    phone_number.sort()
    print('Case #%d: %s' %(tt+1, ''.join(phone_number)) )
