def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def findunit(n):
    for i in range(2,n):
        if n%i == 0:
            return i

x = open('test.in')
get_bin = lambda x, n: format(x, 'b').zfill(n)
y = x.read()
final = []
temp = ''
for i in range(len(y)):
    if y[i] == ' ' or y[i] == "\n":
        temp = int(temp)
        final.append(temp)
        temp = ''
    else:
        temp += y[i]
        if i == len(y)-1:
            final.append(int(temp))
        continue
print (final)
binary = []
for i in range(2**final[0]):
    temp = get_bin(i, final[0])
    if temp[len(temp)-1] == '0' or temp[0] == '0':
        continue
    temparray = []
    for r in range (2,11):
        tempo = int(temp, r)
        value = isPrime(tempo)
        if value:
            break
        else:
            temparray.append(tempo)
    if len(temparray) == 9:
        print (temp, end=' ')
        for rew in temparray:
            print (str(findunit(rew)), end=' ')
        print('')
    
