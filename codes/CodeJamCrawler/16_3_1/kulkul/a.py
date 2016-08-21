def is_valid(parties):
    max_party_people = max(parties)
    sum_party_people = sum(parties)
    if max_party_people / sum_party_people > 0.5:
        return False
    return True


def find_solution(parties, pickup):
    if sum(parties) <= 2:
        people = ''
        for i in range(len(parties)):
            if parties[i] >= 1:
                people += chr(ord('A') + i) * parties[i]
        pickup.append(people)
        return ' '.join(pickup)

    max_party_people = max(parties)
    max_party = parties.index(max_party_people)

    for i in range(min(2, max_party_people), 0, -1):
       next_parties = parties.copy()
       next_parties[max_party] -= i
       if is_valid(next_parties):
           pickup.append(chr(ord('A') + max_party) * i)
           return find_solution(next_parties, pickup)

    max_party2 = parties.index(max_party_people, max_party + 1)
    next_parties = parties.copy()
    next_parties[max_party] -= 1
    next_parties[max_party2] -= 1

    if is_valid(next_parties):
           pickup.append(chr(ord('A') + max_party) * 1 + chr(ord('A') + max_party2) * 1)
           return find_solution(next_parties, pickup)

def test():
    print("---Start Test---")

    test_cases_in = [
        [2, 2],
        [3, 2, 2],
        [1, 1, 2],
        [2, 3, 1],
        [1],
        [1, 2],
        [1, 3],
    ]
    test_cases_out = [
        'AB BA',
        'AA BC C BA',
        'C C AB',
        'BA BB CA',
        'A',
        'B AB',
        'BB AB'
    ]

    for i in range(len(test_cases_in)):
        solution = find_solution(test_cases_in[i], [])
        try:
            assert (solution == test_cases_out[i])
        except:
            print("%d : expected %s, but actual %s" %
                  (i, test_cases_out[i], solution))

    print("---End Test---")

# test()

T = int(input())

for t in range(T):
    P = int(input())
    parties = [int(x)for x in input().split()]
    solution = find_solution(parties, [])

    output_text = "Case #{}: {}".format(t + 1, solution)
    print(output_text)
