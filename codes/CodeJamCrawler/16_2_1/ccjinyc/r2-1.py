__author__ = 'jin-yc10'

inputs = """
100
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER
TWOTOWTWTOWWOTTOOW
IFESIXV
EONNESENRFENIVOU
NOENNENIEXOIS
ONOONENONENNEEOEOE
EOEEEVHTRFRNUS
EVINOENNSENEOEN
ZOOREREZ
SFEEERFXSVUVIOIN
EENVETEFOSNHIEIGV
NEOONINREUF
SXEUIVRORSEOUFFN
IIOEXSNENSOX
EEIEENOZEFVRNOVSEINN
THISEEISXGVFVNIEE
SEVNE
NNENONIEINEINNOEEN
IOEOSNXNE
ETWOETONEISGNHOVWET
HTERE
WRETXOEWIOZVEOSSNT
HTGIHEEITG
HFTEEGEOUROINROZ
OINEEONENNONENNEI
NNNOEIIEINEENNNNIEN
VTEINEFEEHORURNNES
EEVIVWOWTTOEOOFFNNEI
HSENZEEVRVITEEFOER
EOTENWEOONEOENNOON
VSEINXNEIESENIVF
EHEHRITGTE
EON
EERHTEON
ITEGH
OUSREIFXVSNE
SSENNEEOVEVNINEEN
UROONFTWOE
ESINNENEVEINVEFO
ZERNESVEO
ERFUUTFOZRORWOO
NINE
IFIVEVFE
WOT
NNIVNEESINEFEEOV
NNHVEEREWERSEOOTOEZT
OZZEZOZEREREREOORZOR
EISETHTREGHWOIXT
RFISOXU
TEGESFVOIENHUR
NTIREHNEE
RFOTOWU
UNFINREO
WOTOWOETOOTTNOWWWT
ONEONEEONONEENO
RHREXHETESTIEOTW
RZOESIX
EVESNEVEENTSRHE
ONENEVES
ETROOUIEGNNINFHE
REEEVRSTFEHUON
RNEOOEZ
ITEGNEHEVORHETFIE
WEOTEOTWOTNOOOWNWT
ENNVFEOIOE
ENO
ORENOZE
FETEWNONIVNIENIEON
XTVWSEOIFI
NNNIENEEENNOEOOO
FOGRENOHTUEI
EHRHOTUNEROEGTFEI
WTO
EREHNITNE
TNOTENEONENOOWOEOW
FEVI
EVSNE
SNISENIVXEEOSX
RHHOERETGTEFIU
EOONTNWOWETONOTOWE
NOVUSEFER
VIFE
EZRO
ZENZOROROZEZREEROEO
IETGH
ENTOOWOSETOEWENONNVE
RZEO
SXIINFEVEIN
VSEEN
HWETNEETORO
NNXVEIINRETSSHEEE
EHTIORVEEINFNEEN
WOIOXSITEIFXNVSE
NNHTEWSETOXEIOIWRT
NONNENENVNEESIEI
NNENIIINNNNEENIENNEI
ONOETW
""".split()

# inputs = """
# 1
# OEFNNHTRIISIEGUX
# """.split()

"""
Case #1: 012
Case #2: 2468
Case #3: 114
Case #4: 3
"""
nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
alphabet = {}
for n in nums:
    for l in n:
        if not alphabet.has_key(l):
            alphabet[l] = 0
        alphabet[l] += 1
# print alphabet

def rec(cnt, t, a, res):
    if t > len(nums)-1:
        sss = 0
        for k in cnt:
            sss += cnt[k]
        if sss == 0:
            ret = []
            for x in a:
                ret.append(x)
            return ret
        else:
            return None
    n = nums[t]
    # print n, cnt, a
    m = len(n)
    cnt_old = {}
    for c in n:
        if c in cnt and cnt[c] > 0:
            if c not in cnt_old:
                cnt_old[c] = cnt[c]
            cnt[c] -= 1
            m -= 1
        else:
            break
    if m == 0:
        ret = rec(cnt, t, a+[t], res)
        if ret:
            return ret
        for c in cnt_old:
            cnt[c] = cnt_old[c]
        return rec(cnt, t+1, a, res)
    else:
        for c in cnt_old:
            cnt[c] = cnt_old[c]
        return rec(cnt, t+1, a, res)

t = int(inputs[0])
# print t
for i in xrange(t):
    res = ''
    cnt = {}
    S = inputs[i+1]
    # print S
    for c in S:
        if not cnt.has_key(c):
            cnt[c] = 0
        cnt[c] += 1
    # print cnt
    x = rec(cnt, 0, [], [])
    print 'Case #%d:'%(i+1), ''.join([str(a)for a in x])