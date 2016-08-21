array = [0] * 10

def process(N):
    global array
    while N > 0:
        array[N%10] = 1
        N /= 10

f = open("/Users/KOCABEY/Desktop/u.in")
data = f.readlines()
f.close()
f = open("/Users/KOCABEY/Desktop/u.txt","w")
test_number = data[0]

for i in range(int(test_number)):
    f.write("Case #" + str(i+1) + ": ")
    for j in range(10):
        array[j] = 0
    N = int(data[i+1])
    number = 1
    if N == 0:
        f.write("INSOMNIA" + "\n")
        continue
    while sum(array) is not 10 and number < 1000:
        process(number * N)
        number += 1
    f.write( str( (number - 1) * N ) + "\n" )
    print (number - 1) * N
