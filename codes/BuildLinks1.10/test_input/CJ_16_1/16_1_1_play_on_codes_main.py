t = int(input())
for x in range(1, t + 1):
    s = input()
    y = s[0]
    for char in s[1:]:
        if ord(char) >= ord(y[0]):  # if closer to last
            y = char + y
        else:
            y = y + char
    print('Case #{}: {}'.format(x, y))
