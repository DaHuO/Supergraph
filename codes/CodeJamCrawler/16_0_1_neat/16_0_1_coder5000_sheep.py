def main():
    t = int(input())
    for i in range(1, t + 1):
        count_sheep(i, input())

def count_sheep(case_number, n):
    currently_seen = set()
    expected = {i for i in range(0,10)}

    if n == 0:
        print('Case #{case}: INSOMNIA'.format(case=case_number))
    else:
        number=n
        while currently_seen != expected:
            for c in str(number):
                currently_seen.add(int(c))
            number+=n
        print('Case #{case}: {answer}'.format(case=case_number, answer=number-n))

if __name__ == "__main__":
    main()
