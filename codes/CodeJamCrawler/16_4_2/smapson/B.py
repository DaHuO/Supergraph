def product(list_of_terms):
  if len(list_of_terms) == 1:
    return list_of_terms[0]
  else:
    linear_term = list_of_terms[0]
    big_term = product(list_of_terms[1:])
    big_term_x0 = [linear_term[0]*x for x in big_term] + [0]
    big_term_x1 = [0] + [linear_term[1]*x for x in big_term]
    k = len(big_term)+1
    return [big_term_x0[i] + big_term_x1[i] for i in range(k)]

N = int(raw_input())
for test_case in range(N):
  [K, N] = [int(x) for x in raw_input().split()]
  probs = sorted([float(x) for x in raw_input().split()])
  possible_answers = []
  for i in range(0,N+1):
    roots = probs[:i] + probs[-N+i:] if i != N else probs[:N]
    linear_terms = [[1-x, x] for x in roots]
    polynomial = product(linear_terms)
    possible_answers.append(polynomial[N/2])
  answer = max(possible_answers)
  print "Case #%s: %.9f"%(test_case+1, answer)
