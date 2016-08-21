def num_of_groups(stack):
        number = 0
        current_group = None
        for pancake in stack:
                if pancake != current_group:
                        number += 1
                        current_group = pancake
        return number

inn = open("inn.txt")
out = open("out.txt", 'w')
T = int(next(inn))
for i in range(T):
        stack = next(inn).strip()
        output = num_of_groups(stack)
        if stack[-1] == '+':
                output -= 1
        out.write("Case #" + str(i + 1) + ": " + str(output) + "\n")
inn.close()
out.close()
