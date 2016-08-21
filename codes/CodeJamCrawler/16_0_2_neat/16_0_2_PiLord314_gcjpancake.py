def pancake(stack):
    flip = 0
    stackold = stack
    stacknew = stackold.replace("--","-").replace("++","+")
    while stackold != stacknew:
        stacknew = stackold
        stackold = stackold.replace("--","-").replace("++","+")
    if stack[-1] == '+':
        flip = -1
    return len(stacknew) + flip



def main():
    t = int(input())
    out = [0]*t
    for i in range(0,t):
        out[i] = pancake(input())

    for i in range(0,len(out)):
        print("Case #" + str(i + 1) + ": " + str(out[i]))
