output = open('b-large-output.txt', 'w')
T = int(input())

for t in range(1, T+1):
    pancake = list(input())
    pancake.reverse()
    old_pancake = pancake
    pancake = [pancake[0]]
    # flatten
    for i in old_pancake:
        if i == pancake[-1]:
            continue
        else:
            pancake.append(i)
    ans = 0
    for i in pancake:
        ans += 2*(i == '-')
    ans -= pancake[-1] == '-'
    print('Case #{0}: {1}'.format(t,ans))
    output.write('Case #{0}: {1}\n'.format(t, ans))