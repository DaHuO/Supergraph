# CodeJam - Qualification 1st Large Input
# author : Ash-Ishh..


N = int(input(""))

for n_iter in range(1,N+1):
    final_ans = "INSOMNIA"
    ans_dic = {}      
    a = int(input(""))
            
    for i in range(1,1000001): #highest limit : 10^6
        ans = a*i
        if ans == 0:
            break
        for each_num in str(ans):      
           if each_num in ans_dic:
               ans_dic[each_num] += 1
           else:
               ans_dic[each_num] = 1
      
           if len(ans_dic) == 10:
               final_ans = ans
               break
        if final_ans != "INSOMNIA":
             break       
 
           
    print("Case #{0}: {1}".format(n_iter,final_ans))
