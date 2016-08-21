# def print_arr(arr):
#     s = ""
#     for a in arr:
#         s += str(a) + " "
#     print(s[:-1])

# def put_col(X, col, arr, N):
#     for i in range(N):
#         if X[i][col] != 0 and X[i][col] != arr[i]:
#             return False
#     for i in range(N):
#         X[i][col] = arr[i]
#     return True

# def put_row(X, row, arr, N):
#     for i in range(N):
#         if X[row][i] != 0 and X[row][i] != arr[i]:
#             return False
#     for i in range(N):
#         X[row][i] = arr[i]
#     return True

# def solve(M, N):
#     M.sort()
#     print (M)

#     X = [[0 for col in range(N)] for row in range(N)]

#     col = 0
#     row = 0
#     # cnt = 0

#     if M[0][0] == M[1][0]:
#         put_row(X, 0, M[0], N)
#         put_col(X, 0, M[1], N)
#         # col += 1
#         # row += 1
#     else:
#         print("missing first")
#         put_row(X, 0, M[0], N)
#         # row += 1
#         # col += 1

#     for arr in M:
#         if row < N and put_row(X, row, arr, N):
#             row += 1
#         elif col < N and put_col(X, col, arr, N):
#             col += 1
#         print(X)

#     print(X)

#     # find missing parts
#     # rows
#     for row in X:
#         if row not in M:
#             print_arr(row)

#     # cols
#     for i in range(N):
#         col = []
#         for j in range(N):
#             col.append(X[j][i])
#         if col not in M:
#             print_arr(col)

def solve2(M, N):
    count = {}
    for arr in M:
        for a in arr:
            if a not in count:
                count[a] = 0
            count[a] += 1
    #print(count)
    # collect odd
    odds = []
    for key in count:
        if count[key] % 2 == 1:
            odds.append(key)
    
    odds.sort()
    return odds

T = int(input())
for t in range(0, T):
    N = int(input())
    M = []
    for n in range(0, 2 * N - 1):
        a = input()
        row = []
        for c in a.split(' '):
            row.append(int(c))
        M.append(row)
    sol = solve2(M, N)
    out = "Case #%s: " % (t+1)
    for a in sol:
        out += str(a) + " "
    print(out[:-1])

