def sort(data,idx=1,reverse=True):
    return sorted(data, key=lambda t:t[idx],reverse=reverse)

def d(data):
    res = {}
    for k,v in data:
        if v in res:
            res[v].append(k)
        else:
            res[v] = [k]
    return res

def valid(data):
    ddd = d(data)
    return len(ddd[max(ddd.keys())])>1

def desc(data, idx):
    res = sort(data,0,False)
    res[idx] = list(res[idx])
    res[idx][1]-=1
    return res

def do(data,res):
    data = sort(data)
    ddd = d(data)
    maxval = max(ddd.keys())
    if maxval <= 0:
        return None, res
    idx = ddd[maxval].pop()
    data = desc(data, idx)
    res[-1].append(chr(idx+ord('A')))
    return data, res

def solve(ip, data):
    res = [[]]
    data = list(enumerate(data))
    while data != []:
        data,res = do(data, res)
        if data is None:
            break
        if valid(data) or len(res[-1])==2:
            res.append([])
    result = ' '.join([
        ''.join(sorted(l))
        for l in res
        if l
    ])
    print("Case #{}: {}".format(ip+1, result))

def main():
    np = int(input())
    for ip in range(np):
        input()
        data = [int(i) for i in input().split(' ')]
        solve(ip,data)

main()
