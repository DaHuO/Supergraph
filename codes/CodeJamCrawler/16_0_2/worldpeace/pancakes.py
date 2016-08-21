f = open('B-large.in', 'r')

# Extract the input
T = int(f.next())
cases = [f.next().strip() for _ in range(T)]  # ['-', '-+', '+-', '+++', '--+-']

f.close()

o = open('output.txt', 'w')

for s, S in enumerate(cases):  # [[0], [0, 1], [1, 0], [1, 1, 1], [0, 0, 1, 0]]

    # Convert "+" to 1 and "-" to 0
    cases[s] = [1 if x is "+" else 0 for x in S]

    stack = cases[s]  # e.g. [0, 0, 1, 0]
    counter = 0

    while sum(stack) != len(stack):

        for i, pancake in enumerate(stack):

            # Check if its in boundaries:
            if (i+1) < len(stack):
                # Check if doesnt match next one:
                if stack[i] != stack[i+1]:
                    # Start from beginning
                    for x in range(i+1):
                        # Toggle
                        stack[x] ^= 1
                    break
            else:
                if sum(stack) != len(stack):
                    for y in range(len(stack)):
                        stack[y] ^= 1

        counter += 1

    o.write("Case #%s: %s\n" % (s + 1, str(counter)))

o.close()
