def get_even_count_numbers(numbers):
    candidates = set([])
    for num in numbers:
        if num in candidates:
            candidates.remove(num)
        else:
            candidates.add(num)
    return sorted(list(candidates))


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        numbers = []
        for j in range(2 * n - 1):
            row = input()
            numbers += list(int(k) for k in row.split())
        answer = get_even_count_numbers(numbers)
        print('Case #{}: {}'.format(i + 1, ' '.join(list(str(k) for k in answer))))


main()