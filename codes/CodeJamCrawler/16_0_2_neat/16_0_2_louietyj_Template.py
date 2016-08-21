with open('B-large (2).in', 'r') as f:
    data = f.read()

data = data.split('\n')
output = []

print(data.pop(0), 'cases.\n')
while data:
    if data[0] == '':
        break
    # ANSWER GOES HERE
    pancakes = data.pop(0)
    curr = pancakes[0]
    count = 0
    for pancake in pancakes:
        if pancake != curr:
            count += 1
            curr = pancake
    if count % 2 == 0:
        # Even flips
        if pancake[0] == '-':
            count += 1
    else:
        # Odd flips
        if pancakes[0] == '+':
            count += 1
    output.append(count)

with open('submission.txt', 'w+') as f:
    i = -1
    for i, answer in enumerate(output):
        f.write("Case #%i: %s\n" % (i+1, answer))
        print("Case #%i: %s" % (i+1, answer))
    print('\n%i cases written to file' % (i+1))
