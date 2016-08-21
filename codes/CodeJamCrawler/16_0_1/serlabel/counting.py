def all_true(array):
    for i in range(len(array)):
        if not array[i]:
            return False
    return True

def count(n):
    digit = [False] * 10
    number = 0
    while not all_true(digit):
        number += n
        aux = number
        while aux != 0:
            digit[aux%10] = True
            aux //= 10
    return number

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        if n == 0:
            print("Case #{}: INSOMNIA".format(i))
        else:
            print("Case #{}: {}".format(i, count(n)))
