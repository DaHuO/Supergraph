from __future__ import absolute_import, division, print_function

nums = {
   0: "ZERO",
   1: "ONE",
   2: "TWO", 3: "THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE"}



def check_saves(save_point):
    while save_point:
        for i in range(-1, 10):
            to_backtrack = save_point.pop(i)

            for row, answer, saved_k in to_backtrack:

                row_snap = row
                answer_snap = answer
                for k in range(saved_k+1, 10):
                    v = nums[k]
                    success = True
                    row = row_snap
                    answer = answer_snap

                    while success:
                        new_row = row
                        for l in v:
                            if l not in new_row:
                                success = False
                                break
                            new_row = new_row.replace(l, '', 1)

                        if success:
                            answer = answer + str(k)
                            row = new_row
                            if row == '':
                                return answer

                            save_point[k].append((row, answer, k)) #if not already there

    raise Exception()


def solve(row):

    save_point = {}
    for i in range(-1, 10):
        save_point[i] = [(row, "", i)]

    ans = check_saves(save_point)
    count = 0
    for c in ans:
        count += len(nums[int(c)])
    if count != len(row):
        raise Exception
    return ans



#with open('a.in') as f:
with open('A-small-attempt3.in') as f:
#with open('A-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        words = f.readline().strip()
        ans = solve(words)

        print('Case #%s: %s' % (str(puzzle_count + 1), ans))
