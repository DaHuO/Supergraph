
T = int(raw_input())
for tc in range(1, T+1):
   K, C, S = map(int, raw_input().split())
   print 'Case #{}:'.format(tc), ' '.join(map(str, range(1, K+1)))
