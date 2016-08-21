def count_reverse(s):
    if s == []:
        return 0
    if s[-1] == False:
        return 1 + count_reverse([not c for c in s[:-1]])
    else:
        return 0 + count_reverse(s[:-1])


t = int(input())
for case in range(1,t+1):
    s = input()
    state = [s[0] == '+']
    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            state.append(s[i] == '+')
    print('Case #'+str(case)+': ' + str(count_reverse(state)))
