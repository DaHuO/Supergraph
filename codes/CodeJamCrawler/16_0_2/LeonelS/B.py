def resolution(chs):
    compr_list = []
    last = ""
    for ch in chs:
        if ch != last:
            last = ch
            compr_list.append(ch)
    if compr_list[0] == "+":
        return (len(compr_list) / 2) * 2 #jaja, ta re cabeza esto pero anda (capaz)
    return 1 + ((len(compr_list)-1) / 2)*2 
        
if __name__ == '__main__':
    tests = int(raw_input())
    for test_case, chs in enumerate(xrange(tests), 1):
        answer = resolution(raw_input())
        print "Case #{}: {}".format(test_case, answer)
        
        
        
        
        
        
        
        
        
        
        
