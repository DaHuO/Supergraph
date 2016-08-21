importResults = list()

while True:
    try:
        text = raw_input()
        if len(text.strip()) == 0:
            break
        else:
            importResults.append(text.strip())
    except EOFError:
        break

def countingSheep(x):
    target_set = set(range(10))
    if x == 0:
        """
        If x is 0, we never get anywhere
        """
        return "INSOMNIA" #TODO: explain why
    else:
        """
        we're not concerned otherwise, because we can always multiply by 2**n*5**m to make it an odd number, and then
         keep multiplying
        """
        current_count = x
        current_set = digits(current_count)
        while current_set != target_set:
            current_count += x
            current_set = current_set.union(digits(current_count))
        return current_count

def digits(x):
    # returns a list of the digits contained in x
    return set(map(int, list(str(x))))

for i in range(len(importResults)):
    if i == 0:
        pass # this corresponds to the number of items
    else:
        print "Case #{case_id}: {result}".format(case_id = i, result = countingSheep(int(importResults[i])))



