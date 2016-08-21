import random
length = 16
quantity = 50
ans = []

def check_prime(num):
    for l in range(2, int(num ** 0.5) + 1):
        if num % l == 0:
            return l
    else:
        return None

all_numbers = set()

while True:
    a = '1'
    for i in range(14):   # 14
        a += str(random.randint(0, 1))
    a += '1'

    lst = []
    for k in range(2, 11):
        number = int(a, k)
        prime_check = check_prime(number)
        if prime_check == None:
            lst = []
            break
        else:
            lst.append(str(prime_check))

    if lst != []:
        all_numbers.add(a + " " + " ".join(lst))
        print(len(all_numbers))
    if len(all_numbers) == 50:
        break

f = open('C', 'w')
f.write("Case #1:")
f.write("\n")

f.write(("\n".join(list(all_numbers))))

f.close()
