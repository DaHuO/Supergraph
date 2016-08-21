#Revenge of the Pancakes

def revengeOfThePancakes(stack,bestFlips=0):
    if "-" not in stack:return bestFlips
    flips=0
    for i in range(len(stack)-1):
        j=i+1
        if stack[i]!=stack[j]:
            stack=flip(stack[:j])+stack[j:]
            flips+=1
    if "+" not in stack:
        stack=flip(stack)
        flips+=1
    if flips<bestFlips or bestFlips==0:
        bestFlips=flips
    return bestFlips
        

def flip(s):
    newS=""
    for c in s[::-1]:
        if c=="+":newS+="-"
        if c=="-":newS+="+"
    return newS


t = int(input())
for m in range(1, t + 1):
  print("Case #%d: %s" %(m,revengeOfThePancakes(input())))
