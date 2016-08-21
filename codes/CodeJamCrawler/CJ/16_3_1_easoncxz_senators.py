

from string import ascii_uppercase as letters

def solve(tally):
    # tally :: Dict Int Int
    while len(tally) > 2:
        big_party_id = max(tally, key=tally.__getitem__)
        yield [big_party_id]
        tally[big_party_id] -= 1
        if not tally[big_party_id]:
            del tally[big_party_id]
    assert len(tally) == 2, repr(tally)
    while sum(v for k, v in tally.items()) > 0:
        yield list(tally.keys())
        for k in tally:
            assert tally[k] > 0, repr(tally)
            tally[k] -= 1

def describe(escape_seq):
    # escape_seq :: Iter (List Int)
    steps = (''.join(
            letters[person]
            for person
            in step)
        for step
        in escape_seq)
    return ' '.join(steps)


t = int(input())
for ti in range(1, t + 1):
    _ = int(input())
    numbers = [int(p) for p in input().split()]
    tally = {i: n for i, n in enumerate(numbers)}
    print("Case #{}: {}".format(
        ti, describe(solve(tally))))
