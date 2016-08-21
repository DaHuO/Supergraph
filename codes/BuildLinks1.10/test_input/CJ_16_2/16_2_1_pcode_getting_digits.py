from collections import defaultdict
def solve(S):
    freq = defaultdict(int)
    for char in S:
        freq[char] +=1
    answer = []
    while "Z" in freq:
        answer.append('0')
        remove_letters("ZERO", freq)
    while "W" in freq:
        answer.append('2')
        remove_letters("TWO", freq)
    while "U" in freq:
        answer.append('4')
        remove_letters("FOUR", freq)
    while "X" in freq:
        answer.append('6')
        remove_letters("SIX", freq)
    while "S" in freq:
        answer.append('7')
        remove_letters("SEVEN", freq)
    while "O" in freq:
        answer.append('1')
        remove_letters("ONE", freq)
    while "F" in freq:
        answer.append('5')
        remove_letters("FIVE", freq)
    while "N" in freq:
        answer.append('9')
        remove_letters("NINE", freq)
    while "G" in freq:
        answer.append('8')
        remove_letters("EIGHT", freq)
    while "T" in freq:
        answer.append('3')
        remove_letters("THREE", freq)

    answer.sort()
    return ''.join(answer)

def remove_letters(S, freq):
    for char in S:
        freq[char] -=1
        if freq[char] == 0:
            freq.pop(char, None)

"""
solutions = []
T = int(raw_input())
for case in xrange(T):
    S = raw_input().strip()
    sol = solve(S)
    solutions.append('Case #'+str((case+1))+': '+str(sol))
#for solution in solutions:
#        print solution
"""
with open("digits.large", 'r') as f:
    T = int(f.readline())
    solutions=[]
    for case in xrange(T):
        S = f.readline().strip()
        sol = solve(S)
        solutions.append('Case #'+str((case+1))+': '+str(sol)) 

with open('getting_digits_out.txt', 'w') as f:
    for s in solutions[:-1]:
        f.write(s)
        f.write("\n")
    f.write(solutions[-1])