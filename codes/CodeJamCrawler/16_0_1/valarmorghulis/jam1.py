f = open("C:\Users\Himan\Desktop\Downloads\A-large.in","r")
other = open("C:\Users\Himan\Desktop\output3.txt","w")

t = int(f.readline())
def markDigits(current, arr):
    current = set(str(current))
    for digit in current:
        arr[int(digit)]=1

def checkAllOne(arr):
    if sum(arr)==10:
        return 1
    else:
        return 0

for i in xrange(t):
    n = int(f.readline())
    if n==0:
        other.write("Case #"+str(i+1)+":"+" INSOMNIA\n")
    else:
        repeat = True
        start=1
        current = n
        arr=[0 for _ in xrange(10)]
        markDigits(current,arr)
        while repeat:
            current+=n
            markDigits(current,arr)
            if checkAllOne(arr):
                other.write("Case #"+str(i+1)+": "+str(current)+"\n")
                repeat = False

other.close()
f.close()
            
            
            
