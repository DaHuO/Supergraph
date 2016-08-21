
# def flip (arr, index):
#     i = 0;
#     j = index;
#     while (i < j):
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#         j -= 1

# def is_sorted (arr):
#     i = 0;
#     for j in range (1, len(arr)):
#         if arr[i] > arr[j]:
#             return False;
#         i += 1
#     return True;

# def pancake_sorting (arr):
#     ans = 0;
#     while (not is_sorted(arr)):
#         print arr
#         while (len(arr) > 0 and arr[-1] == 1):
#             arr.pop();
#         for i in range (0, len(arr)):
#             if (arr[i] == 1):
#                 print "deu flip", 
#                 flip (arr, i);
#                 print arr
#                 if i != 0:
#                     ans += 1;
#                 if (not is_sorted (arr)):
#                     print "not ",
#                     print arr
#                     flip (arr, len(arr)-1)
#                     ans += 1;
#                 break
    # return ans + 1;

if __name__ == '__main__':
    t = map(int, raw_input().split())[0];
    
    for i in range(t):
        s = raw_input();
        print "Case #%d:" % (i+1),
        # arr = [1 if j == '+' else 0 for j in s]
        # if arr == [1]*len(s):
            # print 0
        # else:
            # print pancake_sorting(arr);
        ans = 0
        if (s[-1] == '-'):
            ans = 1;
        for i in range (len(s)-2, -1, -1):
            if (s[i] != s[i+1]):
                ans += 1
        print ans