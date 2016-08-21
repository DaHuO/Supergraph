import math

#기본적인 동전 제작
def base_coin(J):

    return 10**(J-1)+1

#위의 동전 다음 동전 제작
def next_coin(coin):

    coin_str=str(coin)

    l=len(coin_str)

    n=0

    for i in range (l-2, 0, -1):

        n+=int(coin_str[i])*(2**(l-2-i))

    n=n+1

    #integer n

    list=[]

    for i in range (1, l-1, 1):

        list.append(n//(2**(l-2-i)))

        n=n%(2**(l-2-i))

    answer="1"

    for items in list:

        answer+=str(items)

    answer+="1"

    return(int(answer))

#소수 판별 (소수이면 1)
def det_prime(n):

    count=0

    for i in range (2, int(math.sqrt(n))+1, 1):

        if (n%i==0):
            count+=1
            break

    if (count==0):
        return 1

    else:
        return 0

#진법 변환
def trans(n,k):

    result=0

    str_n=str(n)
    l=len(str_n)

    for i in range (0,l,1):
        result+=int(str_n[i])*(k**(l-1-i))

    return result

#동전이 유효한지 판별 (유효 : 0 반환)
def determine(coin):

    result=0

    list
    #k-jinbup

    for k in range (2,11,1):
        target=trans(coin,k)

        result+=det_prime(target)

    return result

#동전에 대한 키 값을 반환
def keycoin(coin):

    result=[]

    for k in range (2,11,1):

        tcoin=trans(coin,k)

        i=2

        while (tcoin%i!=0):

            i+=1

        result.append(i)

    return result

COUNT=0

N=16 #length
J=50 #num we need

coin=base_coin(N)

coinlist=[]

#동전 리스트를 뽑아냄
while (COUNT!=J):

    D=determine(coin)

    if (D==0):
        coinlist.append(coin)
        COUNT+=1

    coin=next_coin(coin)

#키값을 뽑아냄

keylist=[]

for items in coinlist:

    keylist.append(keycoin(items))

resultline=[]

#출력할거
for i in range (0,len(coinlist),1):

    k1=str(coinlist[i])

    k2=""

    for j in range (0,9,1):
        k2+=" "+str(keylist[i][j])

    k1+=k2

    k1+="\n"

    resultline.append(k1)


f=open("result3.txt", 'w')

f.writelines("Case #1:\n")

for items in resultline:

    f.writelines(items)

f.close()
