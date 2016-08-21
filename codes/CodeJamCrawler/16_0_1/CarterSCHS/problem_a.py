def main():
    answers = []
    for case in range(int(input())):
        n = int(input())
        counts = [0] * 10
        mult_by = 0
        while not all(x >= 1 for x in counts):
            mult_by += 1
            for digit in str(n * mult_by):
                counts[int(digit)] += 1
            if n * mult_by == n * (mult_by + 1):
                break
        if all(x >= 1 for x in counts):
            answers.append(n * mult_by)
        else:
            answers.append('INSOMNIA')
    for i, a in enumerate(answers):
        print('Case #{}: {}'.format(i + 1, a))

if __name__ == '__main__':
    main()
