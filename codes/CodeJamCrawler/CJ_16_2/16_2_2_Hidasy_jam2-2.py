import sys

data = sys.stdin.read().split('\n')
test_cases = data[0]
for index, test_case in enumerate(data[1:]):
    min_diff = 100000000000000
    resp = (100000000, 1000000000)
    coders = test_case.split(" ")[0]
    nc = len([x for x in coders if x == '?'])
    try:
        jammers = test_case.split(" ")[1]
    except:
        break
    nj = len([x for x in jammers if x == '?'])
    for c_comp in range(0, 10**(nc)):
        cd_comp = str(c_comp).zfill(nc)
        new_coders = list(coders)
        cd_comp_i = 0
        for i in range(len(coders)):
            if new_coders[i] == '?':
                new_coders[i] = cd_comp[cd_comp_i]
                cd_comp_i += 1
        new_coders = ''.join(new_coders)
        new_coders_int = int(new_coders)
        for j_comp in range(0, 10**(nj)):
            jd_comp = str(j_comp).zfill(nj)
            new_jammers = list(jammers)
            jd_comp_i = 0
            for i in range(len(jammers)):
                if new_jammers[i] == '?':
                    new_jammers[i] = jd_comp[jd_comp_i]
                    jd_comp_i += 1
            new_jammers = ''.join(new_jammers)
            new_jammers_int = int(new_jammers)
            if abs(new_jammers_int - new_coders_int) < min_diff:
                min_diff = abs(new_jammers_int - new_coders_int)
                resp =  (new_coders, new_jammers)
            if abs(new_jammers_int - new_coders_int) == min_diff:
                if new_coders_int < int(resp[0]) or (new_coders_int == int(resp[0]) and new_jammers_int < int(resp[1])):
                    min_diff = abs(new_jammers_int - new_coders_int)
                    resp = (new_coders, new_jammers)
    print("Case #{}: {}".format(index+1, ' '.join(resp)))
