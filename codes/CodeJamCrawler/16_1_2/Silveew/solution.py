
import numpy as np  # http://www.scipy.org/scipylib/download.html

def read_int(): return int(raw_input())
def read_pair_list(): return [(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in raw_input().split()]
def read_int_list(): return [int(x) for x in raw_input().split()]
def read_pair(): return [int(x) for x in raw_input().strip().split(',')]
def read_string(): return raw_input().strip()


def parse_input():
  T = read_int()
  cases = []
  for _ in xrange(T):
    N = read_int()
    rows = [read_int_list() for _ in xrange(N+N-1)]
    cases.append((N, rows))
  return cases


def try_solve_rec(res, rows, cur_iter):
  # Find two rows with minimal value on cur_iter position
  cur_iter_pos_values = rows[:, cur_iter]
  min_value = min(cur_iter_pos_values)
  cur_rows = [row for row in rows if row[cur_iter] == min_value]
  other_rows = np.array([row for row in rows if row[cur_iter] != min_value])

  # Two possible cases
  assert len(cur_rows) in (1, 2)
  if len(cur_rows) == 2:
    row_1, row_2 = cur_rows
    # try row_1 horiz
    if (row_1[:cur_iter]==res[cur_iter, :cur_iter]).all() and (row_2[:cur_iter] == res[:cur_iter, cur_iter]).all():
      res[cur_iter, cur_iter:] = row_1[cur_iter:]
      res[cur_iter:, cur_iter] = row_2[cur_iter:]
      try_1 = try_solve_rec(res, other_rows, cur_iter+1)
      if try_1: return try_1
    # swap rows
    row_2, row_1 = row_1, row_2
    if not (row_1==row_2).all() and (row_1[:cur_iter]==res[cur_iter, :cur_iter]).all() and (row_2[:cur_iter] == res[:cur_iter, cur_iter]).all():
      res[cur_iter, cur_iter:] = row_1[cur_iter:]
      res[cur_iter:, cur_iter] = row_2[cur_iter:]
      try_2 = try_solve_rec(res, other_rows, cur_iter+1)
      if try_2: return try_2
    # Neither options worked
    return None

  else:
    # Do the same thing reversed to solve this thing
    return try_solve_rev_rec(res, rows, cur_iter, len(res) - 1)
  return None


def try_solve_rev_rec(res, rows, iter_first, cur_iter):
  # Find maximal values
  cur_iter_pos_values = rows[:, cur_iter]
  max_value = max(cur_iter_pos_values)
  cur_rows = [row for row in rows if row[cur_iter] == max_value]
  other_rows = np.array([row for row in rows if row[cur_iter] != max_value])

  # Two possible cases

  assert len(cur_rows) in (1, 2)
  if len(cur_rows) == 2:
    row_1, row_2 = cur_rows
    # try row_1 horiz
    res_row = res[cur_iter, :]
    res_col = res[:, cur_iter]
    if ((row_1[:iter_first]==res_row[:iter_first]).all()
        and (row_1[cur_iter+1:]==res_row[cur_iter+1:]).all()
        and (row_2[:iter_first] == res_col[:iter_first]).all()
        and (row_2[cur_iter+1:] == res_col[cur_iter+1:]).all()):
      res[cur_iter, iter_first:cur_iter+1] = row_1[iter_first:cur_iter+1]
      res[iter_first:cur_iter+1, cur_iter] = row_2[iter_first:cur_iter+1]
      try_1 = try_solve_rev_rec(res, other_rows, iter_first, cur_iter-1)
      if try_1: return try_1
    # swap rows
    row_2, row_1 = row_1, row_2
    if (not (row_1==row_2).all()
        and (row_1[:iter_first]==res_row[:iter_first]).all()
        and (row_1[cur_iter+1:]==res_row[cur_iter+1:]).all()
        and (row_2[:iter_first] == res_col[:iter_first]).all()
        and (row_2[cur_iter+1:] == res_col[cur_iter+1:]).all()):
      res[cur_iter, iter_first:cur_iter+1] = row_1[iter_first:cur_iter+1]
      res[iter_first:cur_iter+1, cur_iter] = row_2[iter_first:cur_iter+1]
      try_2 = try_solve_rev_rec(res, other_rows, iter_first, cur_iter-1)
      if try_2: return try_2# Neither options worked
    return None
  else:
    assert cur_iter == iter_first
    cur_row = cur_rows[0]
    res[cur_iter, cur_iter] = cur_row[cur_iter]
    opt1 = res[cur_iter,:]
    opt2 = res[:, cur_iter]
    if not ((opt1 == cur_row).all() or (opt2 == cur_row).all()):
      return None
    if (opt1 == cur_row).all():
      return list(opt2)
    else:
      assert not (opt1 == cur_row).all()
      return list(opt1)

def solve_case(args):
  N, rows = args
  res = np.zeros((N, N)).astype(int)
  rows = np.array(rows)
  return try_solve_rec(res, rows, 0)

if __name__ == '__main__':
  for idx, args in enumerate(parse_input()):
    res = solve_case(args)
    print 'Case #%d:' % (idx + 1), ' '.join(map(str, res))
