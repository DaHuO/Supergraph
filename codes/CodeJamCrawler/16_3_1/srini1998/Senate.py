t = int(raw_input())  # number of cases
for i in xrange(1, t + 1):
    num_parties = int(raw_input())
    member_nums = raw_input().split(' ')
    member_nums = [int(k) for k in member_nums]
    tot_mems = 0
    for j in range(0,len(member_nums)):
        tot_mems += member_nums[j]
    #print tot_mems
    ret_str = ''
    if tot_mems%2 != 0:
        max_value = max(member_nums)
        max_index = member_nums.index(max_value)
        ret_str+= chr(max_index+65)+' '
        member_nums[max_index] = member_nums[max_index] - 1
        tot_mems -= 1
        
    while tot_mems>0:
        max_value = max(member_nums)
        max_index = member_nums.index(max_value)
        ret_str+= chr(max_index+65)
        member_nums[max_index] = member_nums[max_index] - 1
        tot_mems -= 1
        
        max_value = max(member_nums)
        max_index = member_nums.index(max_value)
        ret_str+= chr(max_index+65)+' '
        member_nums[max_index] = member_nums[max_index] - 1
        tot_mems -= 1
            
        if max(member_nums) > int(tot_mems / 2):
            print str(max(member_nums))+" "+ str(int(tot_mems/2))+" something wrong"
            
    print "Case #"+str(i)+": "+ret_str
        
        