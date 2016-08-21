import string

up = string.ascii_uppercase

def check_majority(parties):
    m = sum(parties) // 2
    for p in parties:
        if p > m:
            return True
    return False

def senate(parties):
    res = ""
    evacuated = 0
    tot = sum(parties)
    while evacuated < tot:
        m1 = max(parties)
        idx = parties.index(m1)
        parties[idx] -= 1
        res += up[idx]
        evacuated += 1

        if m1 in parties:
            idx2 = parties.index(m1)
            parties[idx2] -= 1
            if not check_majority(parties):
                res += up[idx2]
                evacuated += 1
            else:
                parties[idx2] += 1
        res += " "
    return res

for t in range(1, int(input())+1):
    input()
    print("Case #{0}: {1}".format(t, senate([int(x) for x in input().split()])))
