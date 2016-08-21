G = {'tot': 0, 'N': 16, 'stop': False, 'J': 500, "result": [], 'result_set': set()}
def mod_table(n):
    for i in range(2, 11):
        print i, '\t'.join(map(str, [i ** j % n for j in range(0, 32)]))
        
def push_result(v, d):
    a = ['0'] * G['N']
    for i in v:
        a[i] = '1'
        a[i+d] = '1'

    result = [''.join(a[::-1])]
    if result[0] not in G['result_set']:
        G['result_set'].add(result[0])
    else:
        return False

    for base in range(2, 11):
        s = 0
        for i in v:
            s += base ** i
        result.append(str(s))
    G['result'].append(' '.join(result))
    return True

def search(top, f, d, s, v):
    if G['tot'] >= G['J']: return
    if push_result(v, d):
        G['tot'] += 1
    for i in range(f, top):
        if i + d < top and i not in s and i + d not in s:
            s.add(i)
            s.add(i + d)
            v.append(i)
            search(top, i + 1, d, s, v)
            v.pop(-1)
            s.remove(i + d)
            s.remove(i)

def solve(N):
    NN = N - 1
    for d in range(1,N):
        if d == NN - d: continue
        search(N, 1, d, set([0, NN - d, d, NN]), [0, NN - d])

def check():
    assert G['tot'] == G['J']
    s = set()
    for i in G['result']:
        nums = i.split()
        s.add(nums[0])
        for b in range(2, 11):
            nn = int(nums[0], base=b)
            assert nn % int(nums[b-1]) == 0
    assert len(s) == G['J']
assert int(raw_input()) == 1
G['N'], G['J'] = map(int, raw_input().split())

solve(G['N'])
check()
print "Case #1:"
print '\n'.join(G['result'])


    