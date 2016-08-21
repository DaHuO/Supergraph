import numpy as np


def sb(t):
    if t == "+":
        return True
    elif t == "-":
        return False


def str_to_bool(input_str):
    return np.array(list(map(sb, list(input_str))))


def flip(cake_stack, N):
    """
    flip the first N pancakes
    """

    new_cake_stack = np.hstack((np.logical_not(cake_stack[0:N][::-1]), cake_stack[N:]))

    return new_cake_stack


def drop_r_plus(c_stake):
    n = c_stake.shape[0]-1

    it = True
    while True:
        if c_stake[n]==True:
            n=n-1
        else:
            break

        if n<0:
            break



    return c_stake[0:n + 1]


def flip_l_plus(c_stake):
    i = 0
    it=True
    while it == True:
        it=c_stake[i]
        i = i + 1

    c_stake[0:i]=False

    return c_stake



def manu(c_stake,flip_count):

    n_c_stake=drop_r_plus(c_stake)
    if n_c_stake.size==0:
        return flip_count

    init=c_stake[0]

    if init==False:
        n_c_stake=np.logical_not(n_c_stake[::-1])
        flip_count+=1
        flip_count=manu(n_c_stake,flip_count)
    else:
        n_c_stake=flip_l_plus(n_c_stake)
        n_c_stake=np.logical_not(n_c_stake[::-1])
        flip_count+=2
        flip_count=manu(n_c_stake,flip_count)

    return flip_count


def test_flip_l_plus():
    cs = flip_l_plus(np.array([True, False, False, True]))
    print(cs)
    cs=flip_l_plus(np.array([False]))
    print(cs)
    cs=flip_l_plus(np.array([True]))
    print(cs)

def test_conv():
    print(str_to_bool("+"))
    print(str_to_bool("---"))
    print(str_to_bool("-+-"))


def test_drop_r_plus():
    cs = drop_r_plus(np.array([False, False, False, True]))
    print(cs)
    cs = drop_r_plus(np.array([False, True, False, True, True]))
    print(cs)
    cs=drop_r_plus(np.array([True]))
    print(cs)
    cs=drop_r_plus(np.array([False]))
    print(cs)

def test_manu():

    count=manu(str_to_bool("-+"),0)
    print(count)
    count=manu(str_to_bool("--+-"),0)
    print(count)
    count=manu(str_to_bool("+-"),0)
    print(count)
    count=manu(str_to_bool("+"),0)
    print(count)


def run_contest(in_file="A-small.in",out_file="B-small.out"):


    fp = open(in_file, 'r')
    op = open(out_file, 'w')
    N = int(fp.readline())

    for i in range(N):

        D = fp.readline().rstrip()

        op.write("Case #%s: " % (i + 1))

        op.write(str(manu(str_to_bool(D),0)))

        op.write("\n")



if __name__ == "__main__":
    # test_conv()

    # print(flip(np.array([True,True,False,False]),3))

    #test_drop_r_plus()

    #test_flip_l_plus()
    #test_manu()

    run_contest(in_file="B-large.in",out_file="B-large.out")
