def can_sleep(N):
    if N==0:
            return "INSOMNIA"
    K = 1
    remaining_digits = set("0123456789")
    while(remaining_digits):
        num = str(N * K)
        for i in num:
            remaining_digits.discard(i)
        K+=1
    return str(N*(K-1))
        
if __name__ == "__main__":
    output = open("output.txt","w")
    with open("input.txt") as f:
        num = int(f.readline())
        for i in range(num):
            num_to_check = int(f.readline())
            output.write("Case #" + str(i+1) + ": " + can_sleep(num_to_check)+"\n")
    output.close()
