def addition(num, add):
    ret = [ ]
    carry = 0;
    for i in range(len(num)):
        a = 0
        if i < len(add): a = add[i]
        remain = (a + num[i] + carry) % 10
        carry = (a + num[i] + carry) / 10
        ret.append(remain)
    if carry==1:
        ret.append(1)
  #  print(num, add, ret)
    return ret


def count(num):
    if num=='0':
        return 'INSOMNIA'
    used = set()
    num = [int(x) for x in num]
    num = num[::-1]
    add = num[:]
    while True:
        for x in num:
            used.add(x)
        if len(used) == 10:
            break
        num = addition(num, add)
    return ''.join(map(str,num[::-1]))

outfile = open('out.out', 'w')

with open('in.in') as infile:
    T = infile.readline()
    for i in range(int(T)):
        N = infile.readline()
        ans = count(N.strip())
        outfile.write('Case #'+str(i+1)+': '+ ans+'\n')
