
# coding: utf-8

# In[1]:

def digits(number):
    return {digit for digit in str(number)}


# In[11]:

def sleep(n):
    number = n
    seen = digits(n)
    all_digits = digits(1234567890)
    max_tries = 2000
    tries = 0
    while seen < all_digits:
        number += n
        tries += 1
        seen.update(digits(number))
        if tries > max_tries:
            return "INSOMNIA"
    return str(number)


# In[16]:

cases = int(input())

for case in range(1, cases+1):
    number = int(input())
    print("Case #{}: {}".format(case, sleep(number)))


# In[ ]:



