with open('B-large.in', 'r') as f:
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        n_list = 2 * N - 1
        report_list = list()
        for i_list in range(n_list):
            l = list(map(int, f.readline().split()))
            report_list.append(l)
        height_list = [0] * 3000
        for l in report_list:
            for h in l:
                height_list[h] += 1
        missing_report = []
        for h, n_h in enumerate(height_list):
            if n_h % 2 == 1:
                missing_report.append(h)
        missing_report.sort()
        print('Case #%d: %s' % (t + 1, ' '.join(map(str, missing_report))))
