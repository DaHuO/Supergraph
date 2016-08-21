
for _ in range(int(input())):
    S = input()
    S_len = len(S)
    flip_count = 0
    for i in range(S_len):
        if i + 1 == S_len:
            if S[i] == '+':
                print('Case #' + str(_ + 1) + ': ' + str(flip_count))
                break
            print('Case #' + str(_ + 1) + ': ' + str(flip_count + 1))
            break
        if S[i] != S[i + 1]:
            flip_count += 1
