nums = {
 "ZERO": 0
, "EIGHT": 8
, "SIX": 6
, "FOUR": 4
, "TWO": 2
, "SEVEN": 7
, "FIVE": 5
, "THREE": 3
, "NINE": 9
, "ONE": 1
}
def solve(S):
    answer = []
    letters = {}
    for l in S:
        if l in letters:
            letters[l] +=1
        else:
            letters[l]= 1
    check_order = ["ZERO", "EIGHT", "SIX", "FOUR", "TWO", "SEVEN", "FIVE", "THREE", "NINE", "ONE"]
    for w in check_order:
        w_letters = {}
        for l in w: # count numbers letters
            if l in w_letters:
                w_letters[l] +=1
            else:
                w_letters[l]= 1
        boo = True #while still finding letters in S
        while boo:
            # check it's there
            for l in w_letters:
                if l not in letters:
                    boo = False
                elif letters[l] < w_letters[l]:
                    boo = False

            if boo: #remove from S
                for l in w_letters:
                    letters[l] -= w_letters[l]

                answer.append(nums[w]) #translate to digit

    answer.sort()
    new_str = map(str, answer)

    final = "".join(new_str)
    return final

if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        S = str(input())
        print("Case #%i: %s" % (case_num, solve(S)))
