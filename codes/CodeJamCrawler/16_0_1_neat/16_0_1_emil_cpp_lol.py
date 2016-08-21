def main():
    T = int(input())
    for it in range(T):
        i = int(input())
        if i == 0:
            result = 'INSOMNIA'
        else:
            used = [False] * 10
            result = 0
            while not all(used):
                result += i
                ar = list(map(int, str(result)))
                for num in ar:
                    used[num] = True

        print('Case #%s: %s' % (it+1, result))

if __name__ == "__main__":
    main()
