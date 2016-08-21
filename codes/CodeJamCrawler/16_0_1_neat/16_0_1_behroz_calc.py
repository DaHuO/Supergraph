def new_digit(n,store):
    if n not in store:
        return True
    else:
        return False

def digit_scan(digit):
    digits = []
    while digit != 0:
        n = digit%10
        digits.append(n)
        digit-=n
        digit/=10
    return digits

def find_number(number):
    if number == 0:
        return 'INSOMNIA'
    store = []
    factor = 0
    while len(store)!=10:
        numb = number*(factor+1)
        factor+=1
        digits = digit_scan(numb)
        for n in digits:
            if new_digit(n, store):
                store.append(n)
    return numb

file = open("A-large.in",'r')
file = file.read().split()
output = open("output.out",'wb')
#T = int(raw_input())
T = int(file[0])
for i in range(T):
    n = int(file[i+1])
    ans = find_number(n)
    print "Case #{}: {}".format(i+1, ans)
    output.writelines("Case #{}: {}\n".format(i+1, ans))
