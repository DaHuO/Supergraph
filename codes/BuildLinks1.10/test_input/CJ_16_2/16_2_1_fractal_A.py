names={0:"ZERO",
        1:"ONE",
        2:"TWO",
        3:"THREE",
        4:"FOUR",
        5:"FIVE",
        6:"SIX",
        7:"SEVEN",
        8:"EIGHT",
        9:"NINE"}

def find_number(S,t):
        letters = {}
        for _t in range(ord('A'), ord('Z')+1):
                letters[chr(_t)]=0
        for l in S:
                letters[l] += 1
        #print letters
        original_number=[]
        x = 0
        while x < 10 and any(letters.values()):
                while x < 10 and any(letters.values()):
                        for l in names[x]:
                                if letters[l]==0:
                                        break
                        else:
                                for _l in names[x]:
                                        letters[_l]-=1
                                original_number.append(x)
                                #print original_number
                                continue
                        x += 1
                                
                if x == 10 and any(letters.values()):
                        x = original_number.pop()
                        while x==9:
                                for _l in names[x]:
                                        letters[_l]+=1
                                x = original_number.pop()
                        for _l in names[x]:
                                letters[_l]+=1
                        x += 1
                        #print "orig:", original_number, "x: ", x
                elif not any(letters.values()):
                        print "Case #%d: %s" % (t, ''.join([str(_x) for _x in original_number]))
                        return
                else:
                        raise Exception("impossible")

T = int(raw_input())

for t in range(1,T+1):
        S = raw_input()
        find_number(S,t)

