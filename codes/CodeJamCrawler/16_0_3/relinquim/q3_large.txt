i_file = open('C-large.in', 'r')
o_file = open('output.txt', 'w')


def isnt_prime(n, base):
    if base == 3 and n % 2 != 0 and n > 2:
        return False
    if n % 2 == 0 and n > 2:
        return 2
    for i in (3, 5, 7):
        if n % i == 0:
            return i
    return False


def find_bases(n):
    answer = ""
    if not isnt_prime(int(n, 3), 3):
        return False
    for i in range(2, 11):
        factors = isnt_prime(int(n, i), i)
        if not factors:
            return False
        else:
            answer += " " + str(factors)
    return answer


T = int(i_file.readline())
for t in range(T):
    o_file.write("Case #" + str(t+1) + ":\n")
    N, J = [int(x) for x in i_file.readline().split(" ")]
    count = 0
    checks = 0
    for i in range(2**(N-2)):
        num = "{0:b}".format(2**(N-1) + 1 + i*2)
        answer = find_bases(num)
        checks += 1
        if answer:
            o_file.write(str(num) + str(answer) + "\n")
            count += 1
        if count == J:
            break

i_file.close()
o_file.close()
