from __future__ import division
inp = '''5100
0
1
2
11
17
134
4
166
20
117
170
64
139
38
160
5
110
95
195
28
182
34
115
143
86
57
158
43
179
99
12
89
46
88
29
149
22
6
91
32
8
150
44
78
193
168
41
59
154
100
27
3
80
96
66
76
90
125
40
102
7
9
21
25
68
157
77
62
155
114
144
151
84
192
200
54
19
141
191
87
159
186
199
48
72
161
169
180
10
120
63
173
111
94
113
196
146
73
124
24'''
out = '''
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076'''

def parse(inp):
     return inp.split('\n')[1:]
    # inp = inp.splice(0)

def findDigits(num):
    digits = []
    while num >= 1:
        newNum = num // 10
        digits += [num - newNum*10]
        num = newNum
    return digits

def addDigits(digits, addition):
    for digit in addition:
        if not digit in digits:
            digits.append(digit)
    return digits

def check(digits):
    for digit in range(10):
        if not digit in digits:
            return False
    return True

def solve(num):
    original, digits = num, []
    for i in xrange(1000):
        tempDigits = findDigits(num)
        digits = addDigits(digits, tempDigits)
        if check(digits):
            return str(num)
        num = num + original
    return 'INSOMNIA'

def run(inp):
    inp = parse(inp)
    out = ''
    for i in range(len(inp)):
        out = out + '\nCase #' + str(i+1) + ': ' + solve(int(inp[i]))
    return out

# print solve(1)
print run(inp)
