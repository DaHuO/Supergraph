import random

f = open('C-small-attempt0.in.txt')
lines = f.readlines()
f.close()

datas = map(lambda x: x.replace("\n",""), lines)[1:]
ans_lines = []

def make_digit(length):
    digit = "1"
    for num in range(length-2):
        if random.random() >= 0.5:
            digit += "1"
        else:
            digit += "0"
    digit += "1"
    return digit

def is_prime(q,k=50):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def get_divisor(number):
    for num in xrange(2,number):
        if number % num == 0:
            return num

# @return: list of 10 number
def convert_digit(digit):
    check_list = []
    for base in xrange(2,11):
        check_num = 0
        for rank in range(len(digit)):
            check_num += int(digit[rank])*base**(len(digit) - 1 - rank)
        check_list.append(check_num)
    return check_list

def solve(data):
    n = int(data.split(" ")[0])
    j = int(data.split(" ")[1])
    ans_list = []
    divisor_list = []
    for _ in range(1000):
        if len(ans_list) != j:
            flag = 0
            digit = make_digit(n)
            divisor_list2 = []
            check_list = convert_digit(digit)
            for check in check_list:
                if is_prime(check):
                    flag = 1
                    break
            if flag == 0:
                for check in check_list:
                    divisor = get_divisor(check)
                    divisor_list2.append(divisor)
                divisor_list.append(divisor_list2)
                ans_list.append(digit)          
        else:
            break
    return ans_list, divisor_list

# main 
for i, data in enumerate(datas):
    ans_lines.append("Case #"+str(i+1)+":"+"\n")
    answer = solve(data)
    ans_coins = answer[0]
    ans_divisor = answer[1]
    for x in range(len(ans_coins)):
        ans_lines.append(ans_coins[x]+" "+" ".join(map(str,ans_divisor[x]))+"\n")


f = open('ans.txt', 'w')
for line in ans_lines:
    f.write(line)
f.close() 
