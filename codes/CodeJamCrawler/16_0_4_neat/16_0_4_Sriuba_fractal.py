inn = open("inn.txt")
out = open("out.txt", 'w')
T = int(next(inn))
for i in range(T):
        finput = next(inn).strip().split()
        K = int(finput[0])
        C = int(finput[1])
        S = int(finput[2])
        
        # every grad student checks if C many of the originals tiles were not
        # gold. 
        if K % C == 0:
                needed = K / C
        else:
                needed = K / C + 1

        if needed > S:
                out.write("Case #" + str(i + 1) + ": IMPOSSIBLE\n")
        else:
                out.write("Case #" + str(i + 1) + ": ")
                last_checked = 0
                while last_checked < K:
                        position = 1
                        for k in range(C):
                                position += last_checked * K**(C - 1 - k) 
                                last_checked += 1
                                if last_checked == K:
                                        break
                        out.write(str(position) + " ")
                out.write("\n")
inn.close()
out.close()
