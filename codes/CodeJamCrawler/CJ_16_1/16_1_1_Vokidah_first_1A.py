def func(word):
    center = word[0]
    end = ""
    for i in range(1, len(word)):
        if word[i] >= center[0]:
            center = word[i] + center
        else:
            end += word[i]
    return center + end


T = int(input())
f = open('workfile', 'w')
for j in range(1, T + 1):
    word = str(raw_input())
    f.write("Case #%s: %s\n" % (j, func(word)))