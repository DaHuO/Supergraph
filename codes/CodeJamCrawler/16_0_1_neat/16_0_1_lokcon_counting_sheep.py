from sys import stdin

def readline_int():
    return int(stdin.readline().rstrip())


def process(num):
    i = 0
    digits = []
    history = []
    while len(digits) != 10:
        value = num * (i + 1)
        i += 1

        if value in history:
            return None

        history.append(value)

        for char in str(value):
            if int(char) not in digits:
                digits.append(int(char))

    return value



def main():
    T = readline_int()

    for t in range(T):
        answer = process(readline_int())

        if not answer:
            print("Case #%d: INSOMNIA" % (t + 1))
        else:
            print("Case #%d: %d" % (t + 1, answer))

if __name__ == "__main__":
    main()
