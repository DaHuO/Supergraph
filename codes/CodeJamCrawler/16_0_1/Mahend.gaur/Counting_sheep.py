num_of_case = int(raw_input())
ans = []
zero_flag = 0

#import pdb; pdb.set_trace()
for i in range(num_of_case):
    num_list = [0,1,2,3,4,5,6,7,8,9]
    num = int(raw_input())
    if num != 0:
        j = 1
        while num_list:
            temp = mul_res = num * j
            while mul_res > 0:
                digit = mul_res % 10
                if digit in num_list:
                    num_list.remove(digit)
                mul_res = mul_res / 10
                
            j += 1
        ans.append("Case #{}: {}".format(i+1, temp))
    else:
        ans.append("Case #{}: INSOMNIA".format(i+1))

for each_res in ans:
    print each_res



