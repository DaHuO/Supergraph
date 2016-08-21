
from collections import Counter

number = [ Counter('ZERO'), Counter('ONE'), Counter('TWO'), Counter('THREE'), Counter('FOUR'),
            Counter('FIVE'), Counter('SIX'), Counter('SEVEN'), Counter('EIGHT'), Counter('NINE') ];


def test(Counter1, Counter2):
    for c in Counter2:
        if Counter1[c] <= 0:
            return False
    return True

def remove(Counter1, Counter2):
    new_Counter = Counter(Counter1)

    for c in Counter2:
        new_Counter[c] -= Counter2[c]

    new_Counter += Counter()

    return new_Counter

def dfs(digit, char_Counter, ans):
    if len(char_Counter) == 0:
        return ans
    for i in range(digit, 10):
        if test(char_Counter, number[i]):
            #print 'char_Counter: %s,  number[%d]:%s' % (''.join(list(char_Counter)), i, ''.join(list(number[i])))
            new_Counter = remove(char_Counter, number[i])
            new_ans = ans + str(i)
            res = dfs(i, new_Counter, new_ans)
            #print 'new_Counter: %s, new_ans:%s, res: %s' % (new_Counter, new_ans, res)
            if res:
                return res
    return False        

def calc(s):
    #print 'Counter(s) = %s' % Counter(s)
    ans = dfs(0, Counter(s), '')
    return ans

T = int(raw_input())
#print 'T: %d' % T

for i in range(0, T):
    #print 'i = %d' % (i+1)
    S = str(raw_input())
    #print 'S = %s' % S
    ans = calc(S)
    print 'Case #%d: %s' % (i+1, ans)


