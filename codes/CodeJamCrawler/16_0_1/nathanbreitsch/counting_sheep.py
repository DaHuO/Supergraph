
def finished(seen):
    done = True
    for i in range(0, 10):
        if i not in seen:
            done = False
    return done

def get_digits(k):
    return [int(i) for i in str(k)]

def find_max_num(n):
    if n == 0:
        return "INSOMNIA"
    k = 0
    digits_seen = []
    while not finished(digits_seen):
        k += n
        for d in get_digits(k):
            if(d not in digits_seen):
                digits_seen.append(d)

    return k



if __name__ == '__main__':
    num_examples = int(input())
    for i in range(0, num_examples):
        n = int(input().strip())
        solution = find_max_num(n)
        print("Case #%s: %s" % (i+1, solution))
