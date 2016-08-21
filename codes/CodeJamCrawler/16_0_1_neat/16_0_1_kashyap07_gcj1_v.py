testcase = int(input())

def get_last_number(n):
    seen = set()
    l = 0
    m = n
    if n==0:
        return 'INSOMNIA'
    else:
        while True:
            if l==10:
                return n-m
            else:
                for i in str(n):
                    if i not in seen:
                        seen.add(i)
                        l = l+1
                n = n + m

for tc in range(1,testcase+1):

    n = int(input())
    print('Case #',tc,': ',get_last_number(n),sep='')
