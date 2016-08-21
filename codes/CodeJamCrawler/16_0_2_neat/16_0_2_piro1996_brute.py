if __name__ == '__main__':
    t = input()
    for p in range(t):
        s = raw_input()

        queue = [(s, 0)]
        prev = [s]

        while len(queue):
            s, cnt = queue[0]
            queue = queue[1:]

            if '-' not in s:
                print 'Case #%d: %d' % (p + 1, cnt)
                break

            for i in range(1, len(s) + 1):
                n = s[:i][::-1].replace('-', ' ').replace('+', '-').replace(' ', '+') + s[i:]
                if n in prev:
                    continue
                queue.append((n, cnt + 1))
                prev.append(n)
