"""
File: B_Revenge_of_the_Pancakes.py

Author: Sung Uk Ryu

Solution for Google Code Jam 2016, Qualification Round:
    B. Revenge of the Pancakes
"""

f = open('B-large.in', 'r')
out = open('B-large.out', 'w')
n = int(f.readline())

def all_neg(s):
    for i in range(len(s)):
        if s[i] == '+':
            return False
    return True

for i in range(1, n+1):
    pancakes = f.readline()
    count = 0
    while pancakes.find('-') != -1:
        flipped = ''
        if all_neg(pancakes):
            count += 1
            break

        for j in range(1, len(pancakes)):
            if pancakes[j-1] != pancakes[j]:
                flipped += '+' * (j+1) if pancakes[j] == '+' else '-' * (j+1)
                flipped += pancakes[j+1:]
                count += 1
                break
        pancakes = flipped

    out.write('Case #%d: %d\n' % (i, count))



f.close()
out.close()

'''
+- 0
-- 1
++ 2

--+- 0
+++- 1
---- 2
++++ 3
'''