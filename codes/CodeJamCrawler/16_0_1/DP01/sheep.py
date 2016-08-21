_name = "A-large"
# Load the file in a list
with open("{}.in".format(_name)) as f:
    data_set = [int(line.rstrip()) for line in f]

# Remove the first entry since we don't really need it.
no_of_tests = data_set.pop(0)
current_test_no = 1

for n in data_set:
    _solved = False
    seen_values = set()
    _itr = 1
    
    while not _solved:
        if n == 0:
            break

        current_value = _itr * n
        seen_values.update([int(i) for i in str(current_value)])
        _itr += 1
        
        if seen_values.issuperset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
            with open("{}.out".format(_name), 'a') as f:
                f.write("Case #{0}: {1}\n".format(current_test_no, current_value))
 
            _solved = True
            current_test_no += 1
            break
    
    if _solved:
        continue

    with open("{}.out".format(_name), 'a') as f:
        f.write("Case #{0}: INSOMNIA\n".format(current_test_no))

    current_test_no += 1
