import string
import os.path
import json


def read_ints(): return map(int, input().strip().split())


def is_complete(s):
    return all(d in s for d in string.digits)


def preprocess():
    answers = {}
    for num in range(10**6 + 1):
        answers[num] = calc_ans(num)
    return answers


def save(answers):
    with open("a-answers.json", "x") as f:
        json.dump(answers, f, indent=2)


def load():
    with open("a-answers.json") as f:
        answers = json.load(f)
        answers = {int(k): val for k, val in answers.items()}
    return answers


def calc_ans(x):
    if x == 0:
        return 'INSOMNIA'
    letter_set = set()
    for coeff in range(1, 100):
        mul = coeff * x
        digits = str(mul)
        for d in digits:
            letter_set.add(d)
        if is_complete(letter_set):
            return mul
    raise Exception("not found!")


def main():
    if os.path.exists("a-answers.json"):
        answers = load()
    else:
        answers = preprocess()
        save(answers)
    n, = read_ints()
    for case in range(n):
        x, = read_ints()
        ans = answers[x]
        print("Case #{}: {}".format(case + 1, ans))

# if __name__ == '__main__':
main()
