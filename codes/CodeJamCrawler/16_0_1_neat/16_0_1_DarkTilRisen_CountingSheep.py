numbers = {1,2,3,4,5,6,7,8,9,0}
def sheep(number):
    if (number == 0):
        return "INSOMNIA"
    count ,sofar= 1,set()
    while sofar != numbers:
        for i in str(number*(count)):
            sofar.add(int(i))
        count+=1
    return (count-1)*number
for i in range(1,int(input())+1):
    print("Case #{}: {}".format(i, sheep(int(input()))))


#Case #1: INSOMNIA
#Case #2: 10
#Case #3: 90
#Case #4: 110
#Case #5: 5076



