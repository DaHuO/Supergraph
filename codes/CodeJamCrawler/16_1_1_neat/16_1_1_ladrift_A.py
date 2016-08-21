n = int(input())
for i in range(n):
    s = input()
    new_str = s[0]
    for ch in s[1:]:
        if ch < new_str[0]:
            new_str = new_str + ch
        elif ch >= new_str[0]:
            new_str = ch + new_str
    print("Case #{}: {}".format(i + 1, new_str))

