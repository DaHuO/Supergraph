t = int(input())
_list= []
while t>=1:
    tt = int(input())
    _list.append(tt)
    t=t-1

_lolz = 1
i = 1
_count=1
for _run in _list:
    _run_list = [1,2,3,4,5,6,7,8,9,0]
    if _run==0:
        print("Case #{}: {}".format(str(_count), "INSOMNIA"))
        _count+=1
    else:
            i=1
            while True:
                _lolz=_run*i
                
                _temp=_lolz
                while _lolz>0:
                    d=_lolz%10           
                    if d in _run_list:
                        _run_list.remove(d)                       
                    _lolz=_lolz//10
                if not len(_run_list):
                    print("Case #{}: {}".format(str(_count), _temp))
                    _count+=1
                    break
                i=i+1
