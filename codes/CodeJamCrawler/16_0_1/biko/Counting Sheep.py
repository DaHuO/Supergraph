
# coding: utf-8

# In[1]:

import itertools
import io
from concurrent.futures import ThreadPoolExecutor


# In[2]:

TEST_INPUT = """5
0
1
2
11
1692"""


# In[3]:

SMALL_INPUT = """100
0
1
2
11
196
197
187
70
9
95
45
55
83
150
89
90
21
144
137
142
39
121
113
26
62
99
35
110
69
164
77
88
3
78
30
12
128
172
159
50
42
117
71
25
96
80
5
155
84
112
34
177
200
8
94
173
103
33
111
81
158
66
38
23
16
162
148
67
63
183
132
145
169
146
7
65
82
40
29
20
116
124
101
166
120
125
179
22
79
107
6
123
129
185
87
4
174
54
10
136"""


# In[4]:

LARGE_INPUT = """100
0
1
2
11
1692
412910
20
8
590388
212958
976147
166
263599
929350
68609
705674
714506
123977
476345
242825
999991
644346
472989
361660
394253
9
416537
969615
576830
717855
34
999993
280545
548702
25
286565
404368
124
639217
867117
999998
10
50068
601091
579484
1000000
135359
999992
6
999997
999995
778391
324999
677643
999999
38725
792404
207268
999996
145205
564038
148619
585414
246262
565572
805448
250487
451786
40
53424
389730
491918
671813
125
200
864140
208250
4
629132
784642
887443
65229
3
7
269501
19418
999994
961312
917725
68017
552173
582253
810974
12500
778785
1250
436064
5
121394
125000"""


# In[5]:

def get_cases(data):
    with io.StringIO(data) as stream:
        num_cases = int(stream.readline())
        for line in stream:
            yield int(line)


# In[6]:

def digits(number):
    return (int(digit) for digit in str(number))


# In[7]:

def solve_case(case):
    if case == 0:
        return None
    
    numbers = (multiplier * case for multiplier in itertools.count(start=1))
    seen = set()
    for number in numbers:
        seen.update(set(digits(number)))
        if len(seen) == 10:
            return number


# In[8]:

with ThreadPoolExecutor() as executor:
    for index, solution in enumerate(executor.map(solve_case, get_cases(LARGE_INPUT)), start=1):
        print("Case #{}: {}".format(index, solution if solution else "INSOMNIA"))

