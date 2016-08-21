a = input()
b = raw_input().split(' ')

N = int(b[0])
J = int(b[1])
num = 2**(N-1) + 1
print 'Case #1:'




def base_checker(numb):
    out = str(numb)
    for i in range(2,11):
        act_numb = 0
        for j in range(N):
            act_numb = act_numb + int(str(numb)[j])*i**(N-j-1)
        result = prime_check(act_numb)

        if result[0] == 1:
            return (0,'No')
        else:

            out = out + ' ' + str(result[1])

    return (1,out)

def prime_check(n):
    i=2
    
    while i <= 10**3:
        if n%i == 0:
            return (0,i,n)
        i+=1

    return (1,0,0)


old_num = num-2

Ner = 0
for i in range(100*(N-2)):
    new_num = old_num + 2
    old_num = new_num

    prin = base_checker(int(bin(new_num)[2:N+3]))
    
    Ner += prin[0]
    if prin[0] == 1:
        print prin[1]
    if Ner == J:
        break
