MAX_PEOPLE = 2

def print_plan(plan):
    def step2str(step):
        return ''.join([chr(x + ord('A')) for x in step])

    return ' '.join(map(step2str, plan))

def solve_case(n, parties, plan):
    if sum(parties) == 0:
        print('Case #{0}: {1}'.format(n, print_plan(plan)))
        return

    current = []
    for i in range(MAX_PEOPLE):
        max_party = max(parties)
        if max_party > 0:
            total = sum(parties) 
            max_idx = parties.index(max_party)
            parties[max_idx] -= 1
            new_max = max(parties)
            if (new_max > (total/2)):
                parties[max_idx] += 1
                continue

            if sum(parties) == 1:
                parties[max_idx] += 1
                if len(current) == 0:
                    for j in range(len(parties)):
                        if parties[j] > 0:
                            current.append(j)
                    parties = [0] * len(parties)
                break

            current.append(max_idx)

    solve_case(n, parties, plan + [current])

def main():
    count = int(input())
    for i in range(count):
        party_count = int(input())
        parties = [int(x) for x in input().split(' ') if len(x) > 0]
        
        solve_case(i+1, parties, [])

if __name__ == '__main__': 
    main()
