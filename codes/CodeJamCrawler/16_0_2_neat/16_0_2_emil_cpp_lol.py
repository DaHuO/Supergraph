def main():
    T = int(input())
    for it in range(T):
        s = input()
        i = 0
        ans = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                ans += 1
                if s[0] == '+':
                    s = '-' + s[1:]
                else:
                    s = '+' + s[1:]
            i += 1

        if s[0] == '-':
            ans += 1

        print('Case #%s: %s' % (it+1, ans))

if __name__ == "__main__":
    main()
