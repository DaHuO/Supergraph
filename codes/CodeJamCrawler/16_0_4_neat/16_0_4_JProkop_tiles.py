def get_soln(tiles, complexity, students):
    return ' '.join(map(str, range(1, students + 1)))


num_problems = int(raw_input())
for i in range(num_problems):
    tiles, complexity, students = map(int, raw_input().split())
    print 'Case #{}: {}'.format(i + 1, get_soln(tiles, complexity, students))