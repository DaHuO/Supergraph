t = int(input())
for count in range(t):
    n = int(input())
    if n==0:
        print("Case #"+str(count+1)+": INSOMNIA")
    else:
        i= 1;
        digit_list = []
        val = n
        while(True):
            digits = list(str(n))
            for digit in digits:
                if not digit in digit_list:
                    digit_list.append(digit)
            if(len(digit_list)==10):
                break
            else:
                i = i+1;
                n = val * i;
        print("Case #"+str(count+1)+": "+str(n))
