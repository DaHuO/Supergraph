# Sage code (python for math nerds)
N = 32
J = 500
def add(number):
    for i in range(1, N-1):
        if(number[i] == 0):
            number[i] = 1
            return
        else:
            number[i] = 0

def factors(number, base):
    sum = 0
    for i in range(N):
        sum += number[i] * (base ** i)
    return list(sum.factor())

number = [1]+[0]*(N-2)+[1]
jamcoins = []
print("Case #1:")
while(len(jamcoins) < J):
    proofs = []
    debug = []
    for i in range(2,11):
        factor_list = factors(number, i)
        if(len(factor_list) == 1 and factor_list[0][1] == 1):
            break
        proofs.append(factor_list[0][0])

    if(len(proofs) == 9):
        print(''.join(map((lambda x: str(x)),reversed(number))) + " " + " ".join(map((lambda x: str(x)), proofs)))
        jamcoins.append(number)
    add(number)
