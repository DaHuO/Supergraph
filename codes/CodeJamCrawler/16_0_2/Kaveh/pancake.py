def sort_pancackes(t):
    bad_pancakes = t[:t.rfind('-')+1]
    if not bad_pancakes:
        return 0
    first_bad = bad_pancakes.find('-')
    moves = 1
    if first_bad > 0:
        bad_pancakes = first_bad * '-' + bad_pancakes[first_bad:]
        moves += 1
    bad_pancakes = bad_pancakes.replace('-', '?').replace('+', '-').replace('?', '+')
    return sort_pancackes(bad_pancakes) + moves


n = int(input())

for i in range(1, n + 1):
    t = input()
    print("Case #{}: {}".format(i, sort_pancackes(t)))

