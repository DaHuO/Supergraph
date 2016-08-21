def restructure(arr):
    newarray = []
    newarray.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            newarray.append(arr[i])
    return newarray

def flipPancake(pancake):
    i = 0
    a = [1,-1]
    b = [-1,1]
    c = [-1]
    d = [1]
    countkey = {'a': 2, 'b': 1, 'c':1, 'd':0}
    arr = []
    for ch in pancake:
        if ch=='+':
            arr.append(1)
        elif ch=='-':
            arr.append(-1)
       # i = i+1
    arr = restructure(arr)
   # print arr
    if(arr==d):
        return countkey['d']
    elif(arr==b or arr==c):
        return countkey['b']
    elif(arr==a):
        return countkey['a']
    else :
        count = 0
        i = 1
        #print arr[i]
        while(arr!=a and arr!=b and arr!=c and arr!=d):
            if(arr[len(arr)-i]==-1):
               # print "unflipped",arr
                for j in range(0,len(arr)-i+1):
                    arr[j] = -arr[j]
                #print "flipped",arr
                count = count+1
                arr = restructure(arr)
                i = 1
               # print "restructered",arr
            else:
                i = i+1
                
        if(arr==d):
            return count+countkey['d']
        elif(arr==b or arr==c):
            return count+countkey['b']
        elif(arr==a):
            return count+countkey['a']

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
#print t
for i in xrange(1, t + 1):
  n = str(raw_input())  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, flipPancake(n))
  # check out .format's specification for more formatting options