import sys
lines = sys.stdin.read().splitlines()
num_tests = int(lines[0])
strings = lines[1:]

for i, s in enumerate(strings):
    out = ""    
    for c in s:
        if out == "": out += c; continue
        if ord(c) >= ord(out[0]): out = c + out
        else: out += c

    sys.stdout.write("Case #%d: %s\n" % (i + 1, out))
