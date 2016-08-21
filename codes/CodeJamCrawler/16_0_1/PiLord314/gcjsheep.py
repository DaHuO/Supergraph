

def sheep(n):
    total = 0;
    nums = [0]*10;
    for i in range(1,1000):
        ni = n*i
        while ni > 0:
            temp = ni%10
            if (nums[temp] == 0):
                nums[temp] = 1
                total += 1
            ni = int(ni//10)
        #print(n*i)
        #print(nums)
        if total == 10:
            return i*n

    return "Insomnia"


def main():
    t = int(input())
    out = [0]*t
    for i in range(0,t):
        out[i] = sheep(int(input()))

    for i in range(0,len(out)):
        print("Case #" + str(i + 1) + ": " + str(out[i]))
