class Solution:

    def __init__(self):
        with open('/Users/zshi/Desktop/A-large.in') as f:
            content = f.readlines()
        self.num_tests = int(content[0].replace('\n',''))
        self.test_cases = []
        for i in xrange(1,self.num_tests+1):
            num = content[i].replace('\n','')
            self.test_cases.append(int(num))
        print len(self.test_cases)

    # pancakes: str -> +++ return 0
    # pancakes --+-       return 3
    def min_flip(self, pancakes):
        total_flips = 0
        cur_pos = 0
        cur_sign, prev_sign = pancakes[0],pancakes[0]
        while cur_pos < len(pancakes):
            cur_sign = pancakes[cur_pos]
            if cur_sign != prev_sign:
                if cur_sign == '+':
                    total_flips += 1
                else:
                    total_flips += 2
                while cur_pos < len(pancakes):
                    if pancakes[cur_pos] != cur_sign:
                        break
                    cur_pos += 1
                prev_sign = '+'
            else:
                cur_pos += 1
                if cur_pos == len(pancakes):
                    break
                prev_sign = cur_sign

        if prev_sign == cur_sign == '-':
            total_flips += 1
        return total_flips

s=Solution()
assert s.min_flip('-')==1
assert s.min_flip('-+')==1
assert s.min_flip('+-')==2
assert s.min_flip('+++')==0
assert s.min_flip('---')==1
assert s.min_flip('--+-')==3
assert s.min_flip('+-+-')==4
assert s.min_flip('++++++--------++--')==4
assert s.min_flip('-+-+')==3



